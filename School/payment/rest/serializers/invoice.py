from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from payment.models import Invoice, InvoiceItem

from SchoolAdminApp.rest.serializers.feesInformation import FeesInformationSerializer
from SchoolAdminApp.models import FeesInformation


class InvoiceItemListSerializer(ModelSerializer):
    fees = FeesInformationSerializer()

    class Meta:
        model = InvoiceItem
        fields = [
            "id",
            "name",
            "description",
            "quantity",
            "amount",
            "discount",
            "total_amount",
            "fees",
        ]


class InvoiceItemPostSerializer(ModelSerializer):
    fees = serializers.SlugRelatedField(
        queryset=FeesInformation.objects.all(),
        slug_field="uid",
        allow_null=True,
        required=False,
    )

    class Meta:
        model = InvoiceItem
        fields = [
            "name",
            "description",
            "amount",
            "quantity",
            "discount",
            "fees",
        ]


class InvoiceListSerializer(ModelSerializer):
    items = InvoiceItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
            "user",
            "issue_date",
            "due_date",
            "total_item",
            "total_amount",
            "total_discount",
            "grand_total",
            "invoice_status",
            "school",
            "student_class",
            "section",
            "invoice_type",
            "fee_for",
            "items",
        ]


class InvoicePostSerializer(ModelSerializer):
    items = InvoiceItemPostSerializer(many=True, write_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
            "user",
            "issue_date",
            "due_date",
            "total_item",
            "total_amount",
            "total_discount",
            "grand_total",
            "invoice_status",
            "school",
            "student_class",
            "section",
            "invoice_type",
            "fee_for",
            "items",
        ]

    def create(self, validated_data):
        invoice_items = validated_data.pop("items", None)
        invoice = super().create(validated_data)
        total_item = 0
        total_invoice_amount = 0
        total_discount = 0
        grand_total = 0
        # create invoice items with invoice items data
        for item in invoice_items:
            name = item.get("name", None)
            description = item.get("description", None)
            amount = (
                item.get("fees", None).fees_amount
                if item.get("fees", None)
                else item.get("amount", None)
            )
            quantity = item.get("quantity")
            discount = item.get("discount", 0.00)
            total_amount = (amount - discount) * quantity
            fees = item.get("fees", None)
            # keep track for invoice
            total_item += quantity
            total_discount += discount
            total_invoice_amount += amount
            grand_total += total_amount

            InvoiceItem.objects.create(
                name=name,
                description=description,
                amount=amount,
                quantity=quantity,
                discount=discount,
                total_amount=total_amount,
                fees=fees,
                invoice=invoice,
            )
        invoice.total_item = total_item
        invoice.total_amount = total_invoice_amount
        invoice.total_discount = total_discount
        invoice.grand_total = grand_total
        invoice.save()
        return invoice
