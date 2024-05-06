from django.db import models

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, serializers

from common.custom_views import CustomRetrieveUpdateDestroyAPIView
from common.choice import Status

from ..serializers.student import (
    StudentInformationListSerializer,
    StudentImageSerializer,
    StudentCurrentStatusSerializer,
    StudentPermanentAddressSerializer,
    StudentPresentAddressSerializer,
    StudentFatherSerializer,
    StudentMotherSerializer,
    StudentGuardianSerializer,
    StudentDetailInformationListSerializer,
    StudentCurrentStatusDetailsSerializer
)

from ...models import (
    Student,
    StudentImage,
    StudentCurrentStatus,
    StudentPermanentAddress,
    StudentPresentAddress,
    StudentFather,
    StudentMother,
    StudentGuardian
)


class StudentInformationListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentInformationListSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        queryset = Student.objects.filter(
            status=Status.Active,
            school_student__slug=school_slug,
        ).select_related("school_student")

        return queryset


class StudentDetail(CustomRetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentInformationListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentInformationListSerializer
        return StudentInformationListSerializer

    def get_queryset(self):
        student = Student.objects.filter(
            status=Status.Active,
        )
        return student


class StudentImageCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentImageSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentImage.objects.filter(
            status=Status.Active,
            student_info__school_student__slug=school_slug,
        ).select_related(
            "student_info"
        )

        return queryset


class StudentImageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentImageSerializer
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
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentImageSerializer
        return StudentImageSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        student_info = StudentImage.objects.filter(
            status=Status.Active,
            student_info__school_student__slug=school_slug,
        ).select_related(
            "student_info"
        )

        return student_info


class StudentCurrentStatusCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentCurrentStatusSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentCurrentStatus.objects.filter(
            status=Status.Active,
            student_current_status__school_student__slug=school_slug,
        ).select_related(
            "student_current_status"
        )

        return queryset


class StudentCurrentStatusRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentCurrentStatusSerializer
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
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentCurrentStatusSerializer
        return StudentCurrentStatusSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentCurrentStatus.objects.filter(
            status=Status.Active,
            student_current_status__school_student__slug=school_slug,
        ).select_related(
            "student_current_status"
        )

        return queryset


class StudentPermanentAddressListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentPermanentAddressSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentPermanentAddress.objects.filter(
            status=Status.Active,
            student_permanent_address__school_student__slug=school_slug,
        ).select_related(
            "student_permanent_address"
        )

        return queryset


class StudentPermanentAddressRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentPermanentAddressSerializer
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
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentPermanentAddressSerializer
        return StudentPermanentAddressSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentPermanentAddress.objects.filter(
            status=Status.Active,
            student_permanent_address__school_student__slug=school_slug,
        ).select_related(
            "student_permanent_address"
        )

        return queryset


class StudentPresentAddressListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentPresentAddressSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentPresentAddress.objects.filter(
            status=Status.Active,
            student_present_address__school_student__slug=school_slug,
        ).select_related(
            "student_present_address"

        )

        return queryset


class StudentPresentAddressRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentPresentAddressSerializer
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
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentPresentAddressSerializer
        return StudentPresentAddressSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentPresentAddress.objects.filter(
            status=Status.Active,
            student_present_address__school_student__slug=school_slug,
        ).select_related(
            "student_present_address"

        )

        return queryset


class StudentFatherListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentFatherSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentFather.objects.filter(
            status=Status.Active,
            student_father__school_student__slug=school_slug,
        ).select_related(
            "student_father"
        )

        return queryset


class StudentFatherRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentFatherSerializer
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
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentFatherSerializer
        return StudentFatherSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentFather.objects.filter(
            status=Status.Active,
            student_father__school_student__slug=school_slug,
        ).select_related(
            "student_father"
        )

        return queryset


class StudentMotherListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentMotherSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentMother.objects.filter(
            status=Status.Active,
            student_mother__school_student__slug=school_slug,
        ).select_related(
            "student_mother"
        )

        return queryset


class StudentMotherRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentMotherSerializer
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

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentMotherSerializer
        return StudentMotherSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentMother.objects.filter(
            status=Status.Active,
            student_mother__school_student__slug=school_slug,
        ).select_related(
            "student_mother"
        )

        return queryset


class StudentGuardianListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentGuardianSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentGuardian.objects.filter(
            status=Status.Active,
            student_guardian__school_student__slug=school_slug,
        ).select_related(
            "student_guardian"
        )

        return queryset


class StudentGuardianRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentGuardianSerializer
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
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentGuardianSerializer
        return StudentGuardianSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentGuardian.objects.filter(
            status=Status.Active,
            student_guardian__school_student__slug=school_slug,
        ).select_related(
            "student_guardian"
        )

        return queryset


class StudentDetailInformationListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentDetailInformationListSerializer

    def get_queryset(self):
        school_slug = self.kwargs['school_slug']

        queryset = Student.objects.filter(
            status=Status.Active,
            school_student__slug=school_slug,
        ).annotate(
            father_name=models.F("student_father_information__name_english_capital"),
            mother_name=models.F("student_mother_information__name_english_capital"),
            village_name=models.F("student_present_address_information__village"),
            post_office_name=models.F("student_present_address_information__post_office"),
            upazila_name=models.F("student_present_address_information__upazila"),
            district_name=models.F("student_present_address_information__district"),
        )

        return queryset
