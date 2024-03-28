from django.db import models
from django.contrib.auth.models import User
from core.models import UniversalModel


# Create your models here.
class InvoiceType(UniversalModel):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Invoice(UniversalModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status_choices = [
        ("Draft", "Draft"),
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Overdue", "Overdue"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default="Draft")
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    class_field = models.ForeignKey(
        Class, on_delete=models.CASCADE, null=True, blank=True
    )
    fee_type = models.ForeignKey(
        FeeType, on_delete=models.CASCADE, null=True, blank=True
    )

    # Add more fields as needed

    def __str__(self):
        return f"Invoice #{self.invoice_number}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    # Add more fields as needed

    def __str__(self):
        return self.description
