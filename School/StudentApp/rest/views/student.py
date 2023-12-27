from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework import status, serializers


from ..serializers import student

from ...models import Student



class StudentInformationListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = student.StudentInformationListSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        queryset = Student.objects.filter(
            school_student__slug=school_slug
        ).select_related('school_student')

        return queryset