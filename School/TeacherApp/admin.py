from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    Teacher,
    TeacherImage,
    
)



class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_teacher',
        'teacher_user',
        'teacher_id',
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
    list_filter = ("teacher_id", 'name', "gender", "date_Of_birth", 'phone', 'joining_date', 'slug',)

admin.site.register(Teacher, TeacherAdmin)


class TeacherImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'teacher_info',
        'image',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('slug',)

admin.site.register(TeacherImage, TeacherImageAdmin)