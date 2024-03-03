from rest_framework import status
from rest_framework.response import Response

from common.custom_views import (
    CustomListCreateAPIView,
    CustomRetrieveUpdateDestroyAPIView,
)

from core.models import ClassAttendance
from core.filters import ClassAttendanceFilter
from core.rest.serializers.attendance import (
    ClassAttendanceListSerializer,
    ClassAttendancePostSerializer,
)
from core.choice import Status


class ClassAttendanceListCreate(CustomListCreateAPIView):
    serializer_class = ClassAttendanceListSerializer
    filterset_class = ClassAttendanceFilter

    def get_queryset(self):
        queryset = ClassAttendance.objects.filter(status=Status.Active).select_related(
            "attendance_class",
            "attendance_section",
            "attendance_student",
            "school",
            "marked_by",
        )
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        else:
            return ClassAttendancePostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            instance = serializer.instance
            list_serializer = ClassAttendanceListSerializer(instance)
            return Response(
                list_serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassAttendanceDetail(CustomRetrieveUpdateDestroyAPIView):
    queryset = ClassAttendance.objects.filter(status=Status.Active)
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClassAttendanceListSerializer
        else:
            return ClassAttendancePostSerializer
