from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, UUIDFilter
from core.models import ClassAttendance


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
