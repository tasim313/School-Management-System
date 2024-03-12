from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    SchoolAdmin,
    SchoolAdminImage,
    Subject,
    ClassTimeTable,
    Department,
    Exam,
    Semester,
    Career,
    EmployeeCandidate,
    Library,
    Transport,
    Hostel,
    SportsInformation,
    Vendor,
    ProductCategory,
    Product,
    PurchaseRequest,
    PurchaseReceived,
    GradingConfig,
    Result,
    HolidayManagement,
    FeesCategory,
    FeesInformation,
    FeesCollection,
)


class SchoolAdminUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_admin',
        'uid',
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
    list_filter = ('name', "gender", "date_Of_birth", 'phone', 'joining_date', 'slug', 'uid',)


admin.site.register(SchoolAdmin, SchoolAdminUserAdmin)


class SchoolAdminImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_admin_info',
        'uid',
        'image',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
    )
    list_filter = ('uid', 'slug',)


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
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Exam, ExamAdmin)


class SemesterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_semester',
        'uid',
        'slug',
        'name',
        'start_date',
        'end_date',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Semester, SemesterAdmin)


class CareerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'title',
        'location',
        'experience',
        'no_of_vacancies',
        'age_limit',
        'salary_from',
        'salary_to',
        'job_type',
        'job_status',
        'start_date',
        'expired_date',
        'description',
        'school_career',
        'career_department',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Career, CareerAdmin)


class EmployeeCandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'name',
        'email',
        'phone_number',
        'portfolio_link',
        'linkedin_link',
        'comment',
        'curriculum_vitae',
        'job_category',
        'school_candidate',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(EmployeeCandidate, EmployeeCandidateAdmin)


class LibraryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'book_id',
        'book_name',
        'language',
        'book_type',
        'book_status',
        'school_library',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Library, LibraryAdmin)


class TransportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_transport',
        'route_name',
        'vehicle_number',
        'driver_name',
        'license_number',
        'contact_number',
        'driver_address',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug',)


admin.site.register(Transport, TransportAdmin)


class HostelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_hostel',
        'block',
        'room_number',
        'room_type',
        'number_of_beds',
        'cose_per_bed',
        'availability',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(Hostel, HostelAdmin)


class SportsInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_sports',
        'sports_id',
        'sports_name',
        'coach_name',
        'started_year',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(SportsInformation, SportsInformationAdmin)


class VendorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_vendor',
        'name',
        'address',
        'phone_number',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(Vendor, VendorAdmin)


class ProductCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_product_category',
        'name',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_product',
        'category',
        'name',
        'description',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(Product, ProductAdmin)


class PurchaseRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_purchase_request',
        'purchase_request_vendor',
        'purchase_request_status',
        'order_date',
        'delivery_date',
        'quantity',
        'amount_tax',
        'payment_method',
        'note_private',
        'note_public',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(PurchaseRequest, PurchaseRequestAdmin)


class PurchaseReceivedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_purchase_received',
        'purchase_received_vendor',
        'purchase_request',
        'purchase_received_status',
        'order_date',
        'delivery_date',
        'partially_received',
        'all_received',
        'amount_tax',
        'payment_method',
        'note_private',
        'note_public',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(PurchaseReceived, PurchaseReceivedAdmin)


class GradingConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_grading',
        'letter_grade_A_plus',
        'letter_grade_A',
        'letter_grade_A_minus',
        'letter_grade_B',
        'letter_grade_C',
        'letter_grade_D',
        'letter_grade_F',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(GradingConfig, GradingConfigAdmin)


class HolidayManagementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'school_holiday',
        'name',
        'holiday_type',
        'holiday_start',
        'holiday_end',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid', 'slug')


admin.site.register(HolidayManagement, HolidayManagementAdmin)


class FeesCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'school_fees',
        'name',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid',)


admin.site.register(FeesCategory, FeesCategoryAdmin)


class FeesInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'fees_category',
        'fess_class',
        'fess_section',
        'fees_amount',
        'fees_start',
        'fees_end',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid',)


admin.site.register(FeesInformation, FeesInformationAdmin)


class FeesCollectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'school_fees_collection',
        'student_fees_collection',
        'fees_collection_category',
        'fees_amount',
        'paid_date',
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )
    list_filter = ('uid',)


admin.site.register(FeesCollection, FeesCollectionAdmin)


class ResultAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        "school_result",
        "result_class",
        "result_section",
        "result_semester",
        "result_subject",
        "result_student",
        "mark",
        "gpa",
        "grade",
        "createdAt",
        "updateAt",
        "user_created",
        "user_updated",
    )

    list_filter = ("uid",)


admin.site.register(Result, ResultAdmin)
