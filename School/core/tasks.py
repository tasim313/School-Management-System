import logging
from tqdm import tqdm
from django.utils import timezone

from celery import shared_task

from common.models import SchoolInformationOnBoarding
from core.models import ClassAttendance
from StudentApp.models import StudentCurrentStatus

logger = logging.getLogger(__name__)

@shared_task
def create_student_attendance_record():
    date = timezone.now().date()
    logger.info(f"Start: Creating attendance record for students on {date}")

    print("Creating attendance record for students")

    school_id_list = SchoolInformationOnBoarding.objects.values_list("id", flat=True)

    for school_id in tqdm(school_id_list):
        students_current_status = StudentCurrentStatus.objects.filter(
            student_current_status__school_student_id=school_id,
        ).select_related(
            "student_current_status",
            "current_class",
            "current_section",
        )

        for student_current_status in students_current_status:
            # Create an instance of ClassAttendance for each student
            attendance_record = ClassAttendance(
                attendance_class_id=student_current_status.current_class.id,
                attendance_section_id=student_current_status.current_section.id,
                attendance_student_id=student_current_status.student_current_status.id,
                school_id=student_current_status.student_current_status.school_student.id,
                date=date,
            )
            # Save the instance to the database
            attendance_record.save()

    logger.info(f"End: Attendance record created for students on {date}")

