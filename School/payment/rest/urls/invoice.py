from django.urls import path, include

from payment.rest.views.invoice import InvoiceListCreate

urlpatterns = [
    path("", InvoiceListCreate.as_view(), name="invoice-list-create"),
]
