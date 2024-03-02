from django.contrib import admin
from SubscriptionApp.models import Subscription, SubscriptionPlan, Transaction
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class SubscriptionPlanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "name",
        "slug",
        "duration_months",
        "price",
        "createdAt",
        "updateAt",
        'user_created',
        'user_updated'
    )

    list_filter = ("uid", "slug",)


admin.site.register(SubscriptionPlan, SubscriptionPlanAdmin)


class SubscriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "school_subscription",
        "plan",
        "start_date",
        "end_date",
        "is_paid",
        "createdAt",
        "updateAt",
        'user_created',
        'user_updated'
    )

    list_filter = ("uid", "slug",)


admin.site.register(Subscription, SubscriptionAdmin)


class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "school_transaction",
        "subscription_plan",
        "amount",
        "transaction_id",
        "invoice_number",
        "account_number",
        "currency",
        "card_type",
        "transaction_status",
        "createdAt",
        "updateAt",
        'user_created',
        'user_updated'
    )

    list_filter = ("uid", "transaction_id", "invoice_number",)


admin.site.register(Transaction, TransactionAdmin)
