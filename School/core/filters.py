from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, UUIDFilter
from django.db.models import DateTimeField, DateField
from django.db.models.functions import Cast
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
    
    def filter_queryset(self, queryset):
        # Filter by exact date if provided
        date_exact = self.request.query_params.get('date_exact')
        if date_exact:
            queryset = queryset.filter(date__date=date_exact)

        return super().filter_queryset(queryset)


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