"""Views for subscription plan model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from SubscriptionApp.models import SubscriptionPlan
from SubscriptionApp.rest.serializers.subscription_plans import SubscriptionPlanSerializer

from common.choice import Status


class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionPlanSerializer

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

    def get_queryset(self):
        queryset = SubscriptionPlan.objects.filter(
            status=Status.Active,
        )

        return queryset


class SubscriptionPlanRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionPlanSerializer
    lookup_field = "uid"

    def get_permissions(self):
        # Don't allow non-authenticated user request via PUT, PATCH, DELETE
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

    def get_queryset(self):
        queryset = SubscriptionPlan.objects.filter(
            status=Status.Active,
        )

        return queryset
