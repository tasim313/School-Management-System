from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    SchoolClass,
    SchoolSection,
    WebsiteInformation,
    SchoolAddressInformation,
    SchoolContactInformation,
    WebsiteHomeSliderContent,
    WebsiteHomeSliderContentFile,
    WebsiteAbout,
    WebsiteAboutFile,
    WebsiteFunFactContent,
    WebsiteAboutWinningAwards,
    SchoolAdmission,
    AcademicInformation
)


class SchoolClassAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_info',
        'name',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_info__name', 'name', 'slug')

admin.site.register(SchoolClass, SchoolClassAdmin)


class SchoolSectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_class',
        'name',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_class__name', 'name', 'slug',)

admin.site.register(SchoolSection, SchoolSectionAdmin)


class WebsiteInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "uid",
        'name',
        'logo',
        'favicon',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('name', 'slug',)

admin.site.register(WebsiteInformation, WebsiteInformationAdmin)


class SchoolAddressInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_address',
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
    list_filter = ('school_address__school_website__name', 'divisions','district','upazila','pourashava','union_parishad','ward','mouza','village','house_holding_number','post_office','post_code', 'slug',)

admin.site.register(SchoolAddressInformation, SchoolAddressInformationAdmin)


class SchoolContactInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_contact',
        'slug',
        'school_contact_address',
        'phone',
        'email',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_contact__school_website__name', 'phone', 'email', 'slug',)

admin.site.register(SchoolContactInformation, SchoolContactInformationAdmin)



class WebsiteHomeSliderContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'website_home_slider_content',
        'slug',
        'title',
        'description',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('website_home_slider_content__school_website__name', 'title', 'slug',)

admin.site.register(WebsiteHomeSliderContent, WebsiteHomeSliderContentAdmin)


class WebsiteHomeSliderContentFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'home_content',
        'slug',
        'image',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('home_content__website_home_slider_content__school_website__name',  'slug',)

admin.site.register(WebsiteHomeSliderContentFile, WebsiteHomeSliderContentFileAdmin)


class WebsiteAboutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'website_about_content',
        'slug',
        'title',
        'short_description',
        'long_description',
        'start_year',
        'years_of_experience',
        'vision',
        'mission',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('website_about_content__school_website__name', 'title', 'slug', 'start_year',)

admin.site.register(WebsiteAbout, WebsiteAboutAdmin)



class WebsiteAboutFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'about',
        'slug',
        'image',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('about__website_about_content__school_website__name', 'about__title', 'slug', 'about__start_year',)

admin.site.register(WebsiteAboutFile,  WebsiteAboutFileAdmin)


class WebsiteFunFactContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'about_info',
        'years_of_experience',
        'number_of_students',
        'number_of_alumni',
        'winning_awards',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('about_info__website_about_content__school_website__name', 'years_of_experience', 'number_of_students', 'number_of_alumni','winning_awards',)

admin.site.register(WebsiteFunFactContent,  WebsiteFunFactContentAdmin)


class WebsiteAboutWinningAwardsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_award',
        'title',
        'awards_image',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_award__website_about_content__school_website__name', 'title',)

admin.site.register(WebsiteAboutWinningAwards,  WebsiteAboutWinningAwardsAdmin)


class SchoolAdmissionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_admission',
        'title',
        'admission_class',
        'admission_branch',
        'admission_division',
        'number_of_seats',
        'limit_of_age',
        'collection_of_prospectus',
        'fill_the_application_form',
        'online_admission_form_date_time',
        'admission_process_college_information_website',
        'digital_lottery_time_information',
        'admission_application_rules',
        'other_description',
        'remark',
        'pdf_file',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_admission__school_website__name', 'title', 'slug',)

admin.site.register(SchoolAdmission,  SchoolAdmissionAdmin)



class AcademicInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'school_academic_information',
        'title',
        'code_of_conducts',
        'guideline_for_parents',
        'dress_code',
        'homework_and_lecture_documents',
        'lesson_plan',
        'academic_calendar',
        'syllabus',
        'class_routine',
        'co_curricular_activities',
        'slug',
        'createdAt',
        'updateAt',
        'user_created',
        'user_updated'
        )
    list_filter = ('school_academic_information__school_website__name', 'title', 'slug',)

admin.site.register(AcademicInformation,  AcademicInformationAdmin)