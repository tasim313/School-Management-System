from common.custom_views import (
    CustomListCreateAPIView,
    CustomRetrieveUpdateDestroyAPIView,
)

from TeacherApp.rest.serializers.teacher import (
    TeacherListDetailSerializer,
    TeacherPostSerializer,
)
from TeacherApp.models import Teacher


class TeacherListCreateAPIView(CustomListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherPostSerializer


class TeacherDetailView(CustomRetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListDetailSerializer
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return TeacherPostSerializer
