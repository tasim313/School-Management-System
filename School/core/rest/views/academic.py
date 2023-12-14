from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


from core.models import AcademicInformation
from core.rest.serializers.academic import AcademicInformationListSerializer


class AcademicInformationList(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AcademicInformationListSerializer

    def get_queryset(self):
        queryset = AcademicInformation.objects.all().order_by("-createdAt")
        return queryset
