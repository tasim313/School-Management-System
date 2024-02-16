from django.urls import include, path

urlpatterns = [
    path(
        "plans/",
        include("SubscriptionApp.rest.urls.subscription_plans"),
    ),
]
