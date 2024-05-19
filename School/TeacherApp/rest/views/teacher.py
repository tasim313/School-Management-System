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

from common.pagination import StandardResultsSetPagination


class TeacherListCreateAPIView(CustomListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListDetailSerializer
    pagination_class = StandardResultsSetPagination

    def get_authenticators(self):
        if self.request.method == "POST":
            return [JWTAuthentication()]
        return super().get_authenticators()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherPostSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        school_slug = self.kwargs.get('school_slug')
        if school_slug:
            queryset = queryset.filter(school_teacher__slug=school_slug).select_related(
                "school_teacher",
                "teacher_user",
            )
        return queryset



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
