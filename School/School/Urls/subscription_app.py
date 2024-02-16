"""Root URL Configuration for SubscriptionApp."""

from django.urls import path, include

urlpatterns = [
     path("api/subscription/", include("SubscriptionApp.rest.urls")),
]