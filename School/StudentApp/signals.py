import logging

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import SchoolClass
from StudentApp.models import StudentCurrentStatus

logger = logging.getLogger(__name__)


@receiver(post_save, sender=StudentCurrentStatus)
def update_student_current_status(sender, instance, created, **kwargs):
    """
    Signal to update the student's current status information.
    This signal will be triggered after a new instance of StudentCurrentStatus is saved.

    Parameters:
        sender (class): The model class that sends the signal (StudentCurrentStatus in this case).
        instance (StudentCurrentStatus): The instance of the model that was just saved.
        created (bool): A boolean indicating whether the instance was created or updated.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        # then update its total student number
        class_id = instance.current_class.id

        try:
            with transaction.atomic():
                class_instance = SchoolClass.objects.get(id=class_id)
                class_instance.total_students += 1
                class_instance.save()
        except SchoolClass.DoesNotExist:
            logger.error("Couldn't update student quantity!")
