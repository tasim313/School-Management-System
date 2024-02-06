from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    Student,
    StudentImage,
    StudentCurrentStatus,
    StudentPermanentAddress,
    StudentPresentAddress,
    StudentFather,
    StudentMother,
    StudentGuardian
)


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "school_student",
        "student_user",
        "middle_name",
        "gender",
        "date_Of_birth",
        "blood",
        "religion",
        "admission_id",
        "phone",
        "slug",
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = (
        "middle_name",
        "gender",
        "date_Of_birth",
        "admission_id",
        "phone",
        "slug",
    )


admin.site.register(Student, StudentAdmin)


class StudentImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "student_info",
        "image",
        "slug",
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = (
        "student_info__school_student__name",
        "student_info__student_user__firstName",
        "student_info__middle_name",
        "student_info__gender",
        "student_info__date_Of_birth",
        "student_info__admission_id",
        "student_info__phone",
        "slug",
    )


admin.site.register(StudentImage, StudentImageAdmin)


class StudentCurrentStatusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "student_current_status",
        "current_class",
        "current_section",
        "slug",
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = (
        "student_current_status__school_student__name",
        "student_current_status__student_user__firstName",
        "student_current_status__middle_name",
        "student_current_status__gender",
        "student_current_status__date_Of_birth",
        "student_current_status__admission_id",
        "student_current_status__phone",
        "slug",
    )


admin.site.register(StudentCurrentStatus, StudentCurrentStatusAdmin)


class StudentPermanentAddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'student_permanent_address',
        'slug',
        'divisions',
        'district',
        'upazila',
        'pourashava',
        'union_parishad',
        'ward',
        'mouza',
        'village',
        'house_holding_number',
        'post_office',
        'post_code',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid',)


admin.site.register(StudentPermanentAddress, StudentPermanentAddressAdmin)


class StudentPresentAddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'student_present_address',
        'slug',
        'divisions',
        'district',
        'upazila',
        'pourashava',
        'union_parishad',
        'ward',
        'mouza',
        'village',
        'house_holding_number',
        'post_office',
        'post_code',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid', )


admin.site.register(StudentPresentAddress, StudentPresentAddressAdmin)


class StudentFatherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "name_bangla",
        "name_english_capital",
        "nid",
        "date_of_birth",
        'birth_certificate_number',
        'phone',
        'occupation',
        'father_status',
        'date_of_death',
        'student_father',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid',)


admin.site.register(StudentFather, StudentFatherAdmin)


class StudentMotherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "name_bangla",
        "name_english_capital",
        "nid",
        "date_of_birth",
        'birth_certificate_number',
        'phone',
        'occupation',
        'mother_status',
        'student_mother',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid', )


admin.site.register(StudentMother, StudentMotherAdmin)


class StudentGuardianAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "name",
        "nid",
        "occupation",
        'guardian_status',
        'phone',
        'student_guardian',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid', )


admin.site.register(StudentGuardian, StudentGuardianAdmin)