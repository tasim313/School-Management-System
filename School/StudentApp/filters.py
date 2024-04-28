"""Filter for Student Rest API"""

from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from core.models import SchoolClass, SchoolSection
from StudentApp.models import Student, StudentCurrentStatus


class StudentCurrentStatusFilter(FilterSet):
    """Filter for the StudentCurrentStatus model."""

    student_uid = CharFilter(
        field_name="student_current_status__uid",
        lookup_expr="iexact",
    )
    class_uid = CharFilter(
        field_name="current_class__uid",
        lookup_expr="iexact",
    )
    section_uid = CharFilter(
        field_name="current_section__uid",
        lookup_expr="iexact",
    )

    def filter_gpa_exact(self, queryset, name, value):
        return queryset.filter(**{name: value})

    class Meta:
        model = StudentCurrentStatus
        fields = [
            "student_uid",
            "class_uid",
            "section_uid",
        ]