from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import PurchaseReceived
from SchoolAdminApp.rest.serializers.purchaseReceived import PurchaseReceivedSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class PurchaseReceivedListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseReceivedSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = PurchaseReceived.objects.filter(
            status=Status.Active,
            school_purchase_received__slug=school_slug,
        ).prefetch_related(
            "school_purchase_received",
            "purchase_received_vendor",
            'product',
            'purchase_request'
        )

        return queryset


class PurchaseReceivedRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseReceivedSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        purchase_received = PurchaseReceived.objects.filter(
            status=Status.Active,
            school_purchase_received__slug=school_slug,
        ).prefetch_related(
            "school_purchase_received",
            "purchase_received_vendor",
            'product',
            'purchase_request'
        )

        return purchase_received
