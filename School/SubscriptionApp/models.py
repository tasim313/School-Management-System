from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone

from SubscriptionApp.choice import TransactionStatus
from SubscriptionApp.utills import (
    get_school_subscription_plan_slug,
    get_school_subscription_slug
)
from common.models import SchoolInformationOnBoarding
from core.models import UniversalModel


# Create your models here.
class SubscriptionPlan(UniversalModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name of the subscription plan."
    )
    slug = AutoSlugField(
        populate_from=get_school_subscription_plan_slug,
        unique=True, null=False, db_index=True
    )
    duration_months = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subscription(UniversalModel):
    school_subscription = models.OneToOneField(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_subscription",
    )
    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.DO_NOTHING,
        related_name="school_subscription_plan",
    )
    slug = AutoSlugField(
        populate_from=get_school_subscription_slug,
        unique=True, null=False, db_index=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def is_active(self):
        return self.is_paid and timezone.now().date() <= self.end_date


class Transaction(UniversalModel):
    """
        This model is used to record transactions associated with school subscriptions,
        including details such as the school, subscription plan, amount, payment status, and transaction information.
    """
    school_transaction = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_transactions",
        help_text="The school associated with this transaction."
    )
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.DO_NOTHING,
        related_name="subscription_plans"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    account_number = models.CharField(max_length=55, null=True)
    card_no = models.CharField(max_length=55, null=True)
    card_type = models.CharField(max_length=150)
    bank_tran_id = models.CharField(max_length=155, null=True)
    currency = models.CharField(max_length=10, default="BDT")
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(
        max_length=10,
        choices=TransactionStatus.choices,
        default="failed"
    )

    def __str__(self):
        return f"{self.school_transaction.name} - {self.subscription_plan.name} - {self.amount} - {self.transaction_status}"
