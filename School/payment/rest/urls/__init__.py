from django.urls import path, include

urlpatterns = [
    path("invoice", include("payment.rest.urls.invoice")),
]
