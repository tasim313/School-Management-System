"""Urls for Bkash Payments REST API."""

from django.urls import path

from SubscriptionApp.rest.views.bkash_payments import (
    BkashPaymentAPI,
)

urlpatterns = [
    path(
        "bkash/",
        BkashPaymentAPI.as_view(),
        name="bkash_payment_api"
    ),
]
