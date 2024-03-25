"""Filter for SchoolAdminApp Rest API"""

from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from SchoolAdminApp.models import Result, Testimonial


class ResultFilter(FilterSet):
    """Filter for the Result model."""

    school_uid = CharFilter(
        field_name="school_result__uid",
        lookup_expr="iexact",
    )
    class_uid = CharFilter(
        field_name="result_class__uid",
        lookup_expr="iexact",
    )
    section_uid = CharFilter(
        field_name="result_section__uid",
        lookup_expr="iexact",
    )
    semester_uid = CharFilter(
        field_name="result_semester__uid",
        lookup_expr="iexact",
    )
    subject_uid = CharFilter(
        field_name="result_subject__uid",
        lookup_expr="iexact",
    )
    student_uid = CharFilter(
        field_name="result_student__uid",
        lookup_expr="iexact",
    )
    mark = NumberFilter(
        field_name="mark",
        lookup_expr="exact",
    )
    gpa = NumberFilter(
        field_name="gpa",
        method="filter_gpa_exact",
    )
    grade = CharFilter(
        field_name="grade",
        lookup_expr="iexact",
    )

    def filter_gpa_exact(self, queryset, name, value):
        return queryset.filter(**{name: value})

    class Meta:
        model = Result
        fields = [
            "school_uid",
            "class_uid",
            "section_uid",
            "semester_uid",
            "subject_uid",
            "student_uid",
            "mark",
            "gpa",
            "grade",
        ]


class TestimonialFilter(FilterSet):
    """Filter for the Testimonial model."""

    school_uid = CharFilter(
        field_name="school_testimonial__uid",
        lookup_expr="iexact",
    )
    student_uid = CharFilter(
        field_name="student_testimonial__uid",
        lookup_expr="iexact",
    )
    student_roll = CharFilter(
        field_name="student_roll",
        lookup_expr="iexact",
    )
    student_reg = CharFilter(
        field_name="student_reg",
        lookup_expr="iexact",
    )
    testimonial_serial_number = CharFilter(
        field_name="testimonial_serial_number",
        lookup_expr="iexact",
    )
    testimonial_issue_date = CharFilter(
        field_name="testimonial_issue_date",
        lookup_expr="exact",
    )

    class Meta:
        model = Testimonial
        fields = [
            "school_uid",
            "student_uid",
            "student_roll",
            "student_reg",
            "testimonial_serial_number",
            "testimonial_issue_date",
        ]
