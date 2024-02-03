"""Helper functions for the SchoolAdminApp app"""

from SchoolAdminApp.models import GradingConfig


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
        return 5.00, "A+"
    if mark >= grade_config.letter_grade_A:
        return 4.00, "A"
    if mark >= grade_config.letter_grade_A_minus:
        return 3.50, "A-"
    if mark >= grade_config.letter_grade_B:
        return 3.00, "B"
    if mark >= grade_config.letter_grade_C:
        return 2.00, "C"
    if mark >= grade_config.letter_grade_D:
        return 1.00, "D"
    else:
        return 0.00, "F"
