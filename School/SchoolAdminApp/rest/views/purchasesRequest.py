from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import PurchaseRequest
from SchoolAdminApp.rest.serializers.purchasesRequest import (
    PurchaseRequestSerializer,
    PurchaseRequestListSerializer,
)

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class PurchaseRequestListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseRequestSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PurchaseRequestSerializer
        else:
            return PurchaseRequestListSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = PurchaseRequest.objects.filter(
            status=Status.Active,
            school_purchase_request__slug=school_slug,
        ).select_related(
            "school_purchase_request",
            "purchase_request_vendor",
        ).prefetch_related(
            "product_request",
            "product_request__category",
        )

        return queryset


class PurchaseRequestRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseRequestSerializer
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

    def get_serializer_class(self):
        if (self.request.method == "PUT" or
                self.request.method == "PATCH"):
            return PurchaseRequestSerializer
        else:
            return PurchaseRequestListSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        purchase_request = PurchaseRequest.objects.filter(
            status=Status.Active,
            school_purchase_request__slug=school_slug,
        ).select_related(
            "school_purchase_request",
            "purchase_request_vendor",
        ).prefetch_related(
            "product_request",
            "product_request__category",
        )

        return purchase_request
