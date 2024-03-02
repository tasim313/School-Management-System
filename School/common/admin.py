from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    SchoolInformationOnBoarding
)


admin.site.site_header = 'Winner Software Solutions administration'
admin.site.index_title = 'Winner Software Solutions'
admin.site.site_title = 'Winner Software Solutions administration'


class SchoolInformationOnBoardingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'name',
        'username',
        'address',
        'phone',
        'school_type',
        'slug',
        'createdAt',
        'updateAt'
        )
    list_filter = ('name', 'phone', )

admin.site.register(SchoolInformationOnBoarding, SchoolInformationOnBoardingAdmin)