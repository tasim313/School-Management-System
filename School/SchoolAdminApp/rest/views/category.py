from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import ProductCategory
from SchoolAdminApp.rest.serializers.category import ProductCategoryListSerializer

from common.choice import Status


class ProductCategoryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCategoryListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = ProductCategory.objects.filter(
            status=Status.Active,
            school_product_category__slug=school_slug,
        ).select_related(
            "school_product_category"
        )

        return queryset


class ProductCategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCategoryListSerializer
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

        product_category = ProductCategory.objects.filter(
            status=Status.Active,
            school_product_category__slug=school_slug,
        ).select_related(
            "school_product_category"
        )

        return product_category
