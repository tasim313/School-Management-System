"""Urls for Bkash Payments REST API."""

from django.urls import path

from SubscriptionApp.rest.views.bkash_payments import (
    BkashPaymentAPI,
    BkashPaymentExecuteAPI
)

urlpatterns = [
    path(
        "bkash/",
        BkashPaymentAPI.as_view(),
        name="bkash_payment_api"
    ),
    path(
        "execute/",
        BkashPaymentExecuteAPI.as_view(),
        name="bkash_payment_execute_api"
    ),
]
