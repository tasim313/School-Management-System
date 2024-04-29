from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, UUIDFilter
from core.models import ClassAttendance, SchoolSection

from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
)


class ClassAttendanceFilter(FilterSet):
    date = DateFromToRangeFilter(field_name="date")
    school = UUIDFilter(
        field_name="school__uid",
        lookup_expr="exact",
    )
    attendance_class = UUIDFilter(
        field_name="attendance_class__uid",
        lookup_expr="exact",
    )

    class Meta:
        model = ClassAttendance
        fields = {
            "date": ["exact"],
            "school": ["exact"],
            "attendance_class": ["exact"],
        }



class SectionFilter(FilterSet):
    """Filter for the section model."""
    
    class_uid = CharFilter(
        field_name="school_class__uid",
        lookup_expr="iexact",
    )
    
    def filter_gpa_exact(self, queryset, name, value):
        return queryset.filter(**{name: value})

    class Meta:
        model = SchoolSection
        fields = [
            "class_uid",
        ]