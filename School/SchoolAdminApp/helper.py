"""Helper functions for the SchoolAdminApp app"""
from django.db.models import Count, Sum, Case, When, IntegerField, Value, F, CharField, OuterRef, Subquery

from SchoolAdminApp.choice import GradeType
from SchoolAdminApp.models import GradingConfig, Result, SchoolResult

from core.choice import Status


def get_gpa_and_grade(mark: int, school_id: int):
    """
    Calculate GPA and corresponding grade based on the given mark and school grading configuration.

    Parameters:
    - mark (int): The student's mark.
    - school_id (int): The ID of the school for which the grading configuration is applied.

    Returns:
    Tuple[float, str]: A tuple containing the calculated GPA and corresponding grade.
    """

    grade_config = GradingConfig.objects.get(
        school_grading_id=school_id
    )

    if mark >= grade_config.letter_grade_A_plus:
        return 5.00, GradeType.A_PLUS

    if mark >= grade_config.letter_grade_A:
        return 4.00, GradeType.A

    if mark >= grade_config.letter_grade_A_minus:
        return 3.50, GradeType.A_MINUS

    if mark >= grade_config.letter_grade_B:
        return 3.00, GradeType.B

    if mark >= grade_config.letter_grade_C:
        return 2.00, GradeType.C

    if mark >= grade_config.letter_grade_D:
        return 1.00, GradeType.D

    else:
        return 0.00, GradeType.F


def get_grade_from_gpa(gpa: float):
    """
    Get the corresponding grade based on the given GPA and school grading configuration.

    Parameters:
    - gpa (float): The student's GPA.
    - school_id (int): The ID of the school for which the grading configuration is applied.

    Returns:
    str: The corresponding grade.
    """
    if gpa == 5.00:
        return GradeType.A_PLUS

    if gpa >= 4.00:
        return GradeType.A

    if gpa >= 3.50:
        return GradeType.A_MINUS

    if gpa >= 3.00:
        return GradeType.B

    if gpa >= 2.00:
        return GradeType.C

    if gpa >= 1.00:
        return GradeType.D

    else:
        return GradeType.F


def calculate_student_cgpa(result: Result):
    """
    Calculate the student's CGPA based on the given result.

    Parameters:
    - result (Result): The student's result.

    Returns:
    SchoolResult: The school result instance.
    """

    queryset = Result.objects.filter(
        school_result_id=result.school_result.id,
        result_class_id=result.result_class.id,
        result_section_id=result.result_section.id,
        result_semester_id=result.result_semester.id,
        result_student_id=result.result_student.id,
        status=Status.Active
    )

    passed_result_ids = queryset.filter(
        gpa__gt=0
    ).values_list('id', flat=True)

    failed_result_ids = queryset.filter(
        gpa=0
    ).values_list('id', flat=True)

    result_data = queryset.aggregate(
        passed_results_count=Count(Case(When(gpa__gt=0, then=1))),
        failed_results_count=Count(Case(When(gpa=0, then=1))),
        total_gpa=Sum('gpa'),
        total_marks=Sum('mark'),
        total_subjects=Count('id')
    )

    failed_results_count = result_data['failed_results_count']
    total_gpa = result_data['total_gpa']
    total_subjects = result_data['total_subjects']

    cgpa = 0 if failed_results_count > 0 or total_subjects == 0 else (
            total_gpa / total_subjects
    )

    grade = get_grade_from_gpa(cgpa)

    # Update or create school result instance
    school_result_instance, created = SchoolResult.objects.update_or_create(
        school_id=result.school_result.id,
        school_class_id=result.result_class.id,
        school_section_id=result.result_section.id,
        school_semester_id=result.result_semester.id,
        school_student_id=result.result_student.id,
        defaults={
            "total_marks": result_data['total_marks'],
            "cgpa": cgpa,
            "grade": grade
        }
    )

    if created:
        school_result_instance.passed_subjects_result.add(*passed_result_ids)
        school_result_instance.failed_subjects_result.add(*failed_result_ids)
    else:
        school_result_instance.passed_subjects_result.set(passed_result_ids)
        school_result_instance.failed_subjects_result.set(failed_result_ids)

    return school_result_instance
