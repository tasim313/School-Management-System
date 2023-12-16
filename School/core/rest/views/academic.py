from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


from core.models import AcademicInformation
from core.rest.serializers.academic import (
    AcademicInformationListSerializer,
    AcademicInformationDetailSerializer,
)


class AcademicInformationList(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AcademicInformationListSerializer

    def get_queryset(self):
        queryset = AcademicInformation.objects.all().order_by("-createdAt")
        return queryset


class AcademicInformationDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AcademicInformationDetailSerializer
    lookup_field = "uid"
    queryset = AcademicInformation.objects.all()

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
