import logging

from celery import shared_task
from django.utils import timezone

from SubscriptionApp.models import Subscription

logger = logging.getLogger(__name__)


@shared_task
def delete_expired_subscriptions():
    logger.info("Deleting expired subscriptions")
    expired_subscriptions = Subscription.objects.filter(
        end_date__lt=timezone.now().date()
    )
    if expired_subscriptions.exists():
        expired_subscriptions.delete()
        logger.info("Expired subscriptions deleted")