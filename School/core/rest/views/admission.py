from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.rest.serializers.admission import (
    SchoolAdmissionSerializer,
    SchoolAdmissionEditSerializer
)
from core.models import SchoolAdmission


class SchoolAdmissionView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolAdmissionSerializer

    def get_queryset(self):
        print("User info: ", self.request.user)
        admission = SchoolAdmission.objects.all()
        return admission


class SchoolAdmissionDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolAdmissionEditSerializer
    queryset = SchoolAdmission.objects.all()
    lookup_field = "uid"