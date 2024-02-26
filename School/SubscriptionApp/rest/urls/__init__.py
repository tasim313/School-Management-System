from django.urls import include, path

urlpatterns = [
    path(
        "plans/",
        include("SubscriptionApp.rest.urls.subscription_plans"),
    ),
    path(
        "bkash/",
        include("SubscriptionApp.rest.urls.bkash_payments"),
    ),
]
