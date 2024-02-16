"""Urls for Subscription REST API."""

from django.urls import path

from SubscriptionApp.rest.views.subscription_plans import (
    SubscriptionPlanListCreateView,
    SubscriptionPlanRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "",
        SubscriptionPlanListCreateView.as_view(),
        name="subscription_plan_list_create"
    ),
    path(
        "<uuid:uid>/",
        SubscriptionPlanRetrieveUpdateDeleteView.as_view(),
        name="subscription_plan_retrieve_update_delete",
    ),
]
