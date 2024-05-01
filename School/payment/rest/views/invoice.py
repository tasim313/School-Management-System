from django.db.models import Prefetch

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from payment.models import Invoice, InvoiceItem
from payment.rest.serializers.invoice import (
    InvoiceItemListSerializer,
    InvoiceListSerializer,
    InvoicePostSerializer,
)


class InvoiceListCreate(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceListSerializer

    def get_queryset(self):
        return Invoice.objects.prefetch_related(
            Prefetch(
                "invoiceitem_set", queryset=InvoiceItem.objects.all(), to_attr="items"
            )
        ).all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return InvoicePostSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            instance = serializer.instance
            list_serializer = InvoiceListSerializer(instance)
            return Response(
                list_serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
