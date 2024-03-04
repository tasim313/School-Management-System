"""Views for Bkash payment gateway."""

import requests

from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from SubscriptionApp.helper import generate_invoice_number
from SubscriptionApp.models import SubscriptionPlan, Subscription, Transaction

from common.models import SchoolInformationOnBoarding


class BkashPaymentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Post method for Bkash payment."""

        plan_uid = request.data.get("plan_uid", "")
        school_username = request.data.get("school_username", "")

        if not plan_uid or not school_username:
            return Response(
                {"error": "Plan UID and School username is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        school: SchoolInformationOnBoarding = SchoolInformationOnBoarding.objects.get(
            username=school_username
        )

        if not school:
            return Response(
                {"error": "School not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        subscription = Subscription.objects.filter(
            school_subscription_id=school.id,
            is_paid=True,
            end_date__gte=timezone.now().date()
        )

        if subscription:
            return Response(
                {"error": "Already subscribed"}, status=status.HTTP_400_BAD_REQUEST
            )

        plan: SubscriptionPlan = SubscriptionPlan.objects.get(
            uid=plan_uid
        )

        if not plan:
            return Response(
                {"error": "Plan not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.grant_token()

        website_base_url = "http://localhost:8000/"

        if response.status_code == 200:
            token = response.json().get("id_token")

            invoice_number = generate_invoice_number()

            request.session[f"bkash_token_{school.username}"] = token
            request.session[f"plan_uid_{school.username}"] = plan_uid
            request.session[f"invoice_number_{school.username}"] = invoice_number

            data = {
                "callbackURL": website_base_url,
                "payerReference": str(school.phone),
                "mode": "0011",
                "amount": str(plan.price),
                "currency": "BDT",
                "intent": "sale",
                "merchantInvoiceNumber": invoice_number,
            }

            response = self.create_payment(data, token)

            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)

            else:
                return Response(
                    "Something went wrong on bkash create payment", status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                "Something went wrong on bkash grant token", status=status.HTTP_400_BAD_REQUEST
            )

    def grant_token(self):
        grant_token_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/grant"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "username": settings.BKASH_USERNAME,
            "password": settings.BKASH_PASSWORD
        }

        body_data = {
            "app_key": settings.BKASH_APP_KEY,
            "app_secret": settings.BKASH_APP_SECRET
        }

        try:
            response = requests.post(
                grant_token_url, headers=headers, json=body_data
            )

        except requests.exceptions.RequestException as e:
            response = Response(
                {"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        return response

    def create_payment(self, data, token):
        create_payment_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": token,
            "x-app-key": settings.BKASH_APP_KEY
        }

        try:
            response = requests.post(
                create_payment_url, headers=headers, json=data
            )
        except requests.exceptions.RequestException as e:
            response = Response(
                {"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        return response


class BkashPaymentExecuteAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Post method for Bkash payment execute."""

        execute_payment_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"

        payment_id = request.data.get("paymentID")
        school_username = request.data.get("school_username")

        token = request.session.get(f"bkash_token_{school_username}")
        plan_uid = request.session.get(f"plan_uid_{school_username}")
        invoice_number = request.session.get(f"invoice_number_{school_username}")

        headers = {
            "Accept": "application/json",
            "Authorization": token,
            "x-app-key": settings.BKASH_APP_KEY
        }

        data = {
            "paymentID": payment_id
        }

        try:
            response = requests.post(
                execute_payment_url, headers=headers, json=data
            )

            if response.status_code == 200:

                school: SchoolInformationOnBoarding = SchoolInformationOnBoarding.objects.get(
                    username=school_username
                )

                if not school:
                    return Response(
                        {"error": "School not found"}, status=status.HTTP_400_BAD_REQUEST
                    )

                plan: SubscriptionPlan = SubscriptionPlan.objects.get(
                    uid=plan_uid
                )

                try:
                    subscription = Subscription.objects.get(
                        school_subscription_id=school.id,
                    )

                    # If school is already subscribed, update the subscription
                    subscription.plan_id = plan.id
                    subscription.start_date = timezone.now().date()
                    subscription.end_date = timezone.now().date() + timedelta(days=plan.duration_months * 30)
                    subscription.is_paid = True
                    subscription.save()

                except Subscription.DoesNotExist:
                    # Subscription does not exist, create a new one
                    Subscription.objects.create(
                        school_subscription_id=school.id,
                        plan_id=plan.id,
                        start_date=timezone.now().date(),
                        end_date=timezone.now().date() + timedelta(days=plan.duration_months * 30),
                        is_paid=True
                    )

                Transaction.objects.create(
                    school_transaction_id=school.id,
                    subscription_plan_id=plan.id,
                    amount=plan.price,
                    transaction_id=payment_id,
                    invoice_number=invoice_number,
                    account_number=school.phone,
                    currency="BDT",
                    card_type="bkash",
                    transaction_status="success"
                )

                return Response(
                    {
                        "message": "Payment successful",
                    },
                    status=status.HTTP_200_OK
                )

        except requests.exceptions.RequestException as e:
            response = Response(
                {"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(response, status=status.HTTP_200_OK)
