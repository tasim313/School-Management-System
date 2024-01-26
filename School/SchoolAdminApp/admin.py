from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    SchoolAdmin,
    SchoolAdminImage,
    Subject,
    ClassTimeTable,
    Department,
    Exam
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


class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_subject',
        'name',
        'uid',
        'subject_id',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid',)


admin.site.register(Subject, SubjectAdmin)


class ClassTimeTableAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_class_time_table',
        'uid',
        'slug',
        'name',
        'school_time_table',
        'school_section_time_table',
        'class_time_table_subject',
        'teacher_id',
        'class_date',
        'class_start_time',
        'class_end_time',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid', 'slug',)


admin.site.register(ClassTimeTable, ClassTimeTableAdmin)


class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_department',
        'uid',
        'name',
        'head_of_department',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid',)


admin.site.register(Department, DepartmentAdmin)


class ExamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_exam',
        'uid',
        'slug',
        'exam_class',
        'exam_section',
        'exam_subject',
        'name',
        'fees',
        'exam_start_time',
        'exam_end_time',
        'exam_date',
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Exam, ExamAdmin)
