from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import FeesCollection
from SchoolAdminApp.rest.serializers.feesCollection import FeesCollectionSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class FeesCollectionListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeesCollectionSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = FeesCollection.objects.filter(
            status=Status.Active,
            school_fees_collection__slug=school_slug,
        ).select_related(
            "school_fees_collection",
            "student_fees_collection",
            "fees_collection_category"
        )

        return queryset


class FeesCollectionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeesCollectionSerializer
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

        fees_collection = FeesCollection.objects.filter(
            status=Status.Active,
            school_fees_collection__slug=school_slug,
        ).select_related(
            "school_fees_collection",
            "student_fees_collection",
            "fees_collection_category"
        )

        return fees_collection
