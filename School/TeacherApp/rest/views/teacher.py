from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from common.custom_views import (
    CustomListCreateAPIView,
    CustomRetrieveUpdateDestroyAPIView,
)

from TeacherApp.rest.serializers.teacher import (
    TeacherListDetailSerializer,
    TeacherPostSerializer,
    TeacherImageSerializer,
)
from TeacherApp.models import Teacher, TeacherImage


class TeacherListCreateAPIView(CustomListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListDetailSerializer

    def get_authenticators(self):
        if self.request.method == "POST":
            return [JWTAuthentication()]
        return super().get_authenticators()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherPostSerializer


class TeacherDetailView(CustomRetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListDetailSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherPostSerializer


class TeacherImageListCreateAPIView(CustomListCreateAPIView):
    queryset = TeacherImage.objects.all()
    serializer_class = TeacherImageSerializer

    def get_authenticators(self):
        if self.request.method == "POST":
            return [JWTAuthentication()]
        return super().get_authenticators()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherImageSerializer


class TeacherImageDetailView(CustomRetrieveUpdateDestroyAPIView):
    queryset = TeacherImage.objects.all()
    serializer_class = TeacherImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherImageSerializer
