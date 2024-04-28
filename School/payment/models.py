import datetime
from django.db import models

from core.models import UniversalModel

from SchoolAdminApp.models import FeesInformation

from common.models import SchoolInformationOnBoarding

from core.models import SchoolClass, SchoolSection

from payment.choices import InvoiceStatus, FeeFor


# Create your models here.
class InvoiceType(UniversalModel):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Invoice(UniversalModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("school_auth.User", on_delete=models.DO_NOTHING)
    issue_date = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    # start of finance related fields
    total_item = models.PositiveBigIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=19, decimal_places=3, default=0.00)
    total_discount = models.DecimalField(max_digits=19, decimal_places=3, default=0.00)
    grand_total = models.DecimalField(max_digits=19, decimal_places=3, default=0.00)
    # end of finance related fields
    invoice_status = models.CharField(
        max_length=10,
        choices=InvoiceStatus,
        default=InvoiceStatus.PENDING,
    )
    school = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    student_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    section = models.ForeignKey(
        SchoolSection,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    invoice_type = models.ForeignKey(
        InvoiceType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    fee_for = models.CharField(
        max_length=10,
        choices=FeeFor,
        default=FeeFor.STUDENT,
    )

    def __str__(self):
        return f"Invoice #{self.id} Fee For: {self.fee_for} Created for: {self.user}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=3)
    price = models.DecimalField(max_digits=19, decimal_places=3)
    discount = models.DecimalField(max_digits=19, decimal_places=3)
    total_price = models.DecimalField(max_digits=19, decimal_places=3)

    fees = models.ForeignKey(
        FeesInformation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    # Add more fields as needed

    def __str__(self):
        return f"ID: {self.id} - Invoice: ({self.invoice})"
