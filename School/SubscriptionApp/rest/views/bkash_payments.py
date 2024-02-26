"""Views for Bkash payment gateway."""

import requests

from django.conf import settings

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class BkashPaymentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Post method for Bkash payment."""

        response = self.grant_token()

        if response.status_code == 200:
            token = response.json().get("id_token")
            data = {
                "callbackURL": "http://localhost/bkash/agreement/callback",
                "payerReference": "01770618575",
                "mode": "0011",
                "amount": "1",
                "currency": "BDT",
                "intent": "sale",
                "merchantInvoiceNumber": "Invoice-002",
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
