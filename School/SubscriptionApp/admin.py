from django.contrib import admin
from SubscriptionApp.models import Subscription, SubscriptionPlan
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

    list_filter = ("uid", "s")

