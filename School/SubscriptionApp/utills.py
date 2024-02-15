from uuid import uuid4

import logging

logger = logging.getLogger(__name__)


def get_school_subscription_plan_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-subscription_plan'}-{str(instance.uid).split('-')[0]}"


def get_school_subscription_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-subscription'}-{str(instance.uid).split('-')[0]}"
