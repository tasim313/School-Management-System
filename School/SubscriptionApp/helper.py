import uuid
import requests

from django.conf import settings
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response


def generate_invoice_number(prefix="INV", length=8, date_format="%Y%m%d"):
    """
    Generate a unique invoice number based on the current date and a unique identifier.

    Returns:
    str: The generated invoice number.
    """
    # Format the current date (e.g., YYYYMMDD)
    date_part = timezone.now().strftime(date_format)

    # Generate a random string as a unique identifier
    unique_part = str(uuid.uuid4().hex)[:length]

    # Combine date and unique parts to form the invoice number
    invoice_number = f"{prefix}-{date_part}-{unique_part}"

    return invoice_number


def grant_token():
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


def create_payment(data, token):
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
