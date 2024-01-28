from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import PurchaseRequest
from SchoolAdminApp.rest.serializers.purchasesRequest import PurchaseRequestSerializer

from common.choice import Status


class PurchaseRequestListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseRequestSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = PurchaseRequest.objects.filter(
            status=Status.Active,
            school_purchase_request__slug=school_slug,
        ).prefetch_related(
            "school_purchase_request",
            "purchase_request_vendor",
            'product_request'
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

    def get_queryset(self):
       
        school_slug = self.kwargs.get("school_slug", None)

        purchase_request = PurchaseRequest.objects.filter(
            status=Status.Active,
            school_purchase_request__slug=school_slug,
        ).prefetch_related(
            "school_purchase_request",
            "purchase_request_vendor",
            'product_request'
        )

        return purchase_request