from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    SchoolAdmin,
    SchoolAdminImage
    
)


class SchoolAdminUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_admin',
        'schoolUser',
        'name',
        'gender',
        'date_Of_birth',
        'phone',
        'joining_date',
        'qualification',
        'experience',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('name', "gender", "date_Of_birth", 'phone', 'joining_date', 'slug',)

admin.site.register(SchoolAdmin, SchoolAdminUserAdmin)


class SchoolAdminImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_admin_info',
        'image',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('slug',)

admin.site.register(SchoolAdminImage, SchoolAdminImageAdmin)