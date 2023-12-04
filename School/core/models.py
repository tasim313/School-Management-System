from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator


from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField


from school_auth.models import User

from common.models import SchoolInformationOnBoarding
from common.models import BaseModel

from .utills import(
    get_school_class_slug,
    get_school_section_slug,
    get_school_address_slug,
    get_school_website_logo,
    get_school_website_favicon,
    get_school_website_slug,
    get_school_contact_slug,
    get_website_home_slider_content_slug,
    get_website_home_slider_content_image,
    get_website_home_slider_content_file_slug,
    get_website_home_slider_content_file_slug,
    get_website_about_slug,
    get_website_about_file_slug,
    get_website_about_file_image,
    get_website_about_file_awards_image,
    get_website_school_admission_slug,
    get_website_school_admission_pdf,
    get_website_school_academic_slug,
    get_website_school_academic_homework_and_lecture_documents_pdf,
    get_website_school_academic_lesson_plan_documents_pdf,
    get_website_school_academic_calendar_documents_pdf,
    get_website_school_academic_syllabus_documents_pdf,
    get_website_school_academic_class_routine_documents_pdf,
    get_website_get_gallery_image,
    get_news_events_slug,
    get_news_events_image
)

from .choice import(
    Status,
    AdmissionClass,
    AdmissionBranch,
    AdmissionDivision,
    NewsEventsStatus,
)


class UniversalModel(BaseModel):
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.Active
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="User_who_created",
        verbose_name="Created Person"
        )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="The_User_who_Updated",
        verbose_name="Updated Person"
    )


class SchoolClass(UniversalModel):
    school_info = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='School_Class_Information')
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=get_school_class_slug, unique=True, null=False, db_index=True)

    class Meta:
        verbose_name_plural = 'School Class'

    def __str__(self):
        return self.name
        



class SchoolSection(UniversalModel):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, related_name='school_class_section')
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=get_school_section_slug, unique=True, null=False, db_index=True)

    class Meta:
        verbose_name_plural = 'School Class Section'


    def __str__(self):
        return self.name 



class WebsiteInformation(UniversalModel):
    school_website = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_website_information')
    name = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    logo = VersatileImageField(upload_to=get_school_website_logo, null=True, blank=True)
    favicon = VersatileImageField(upload_to=get_school_website_favicon, null=True, blank=True)
    slug = AutoSlugField(populate_from=get_school_website_slug, unique=True, null=False, db_index=True)

    class Meta:
        verbose_name_plural = 'School Website Information'

    def __str__(self):
        return self.name




class SchoolAddressInformation(UniversalModel):
    school_address = models.ForeignKey(WebsiteInformation, on_delete=models.DO_NOTHING, related_name='school_address_information')
    slug = AutoSlugField(populate_from=get_school_address_slug, unique=True, null=False, db_index=True)
    divisions = models.CharField(max_length=255, blank=True, null=True)
    district  = models.CharField(max_length=255, blank=True, null=True)
    upazila  = models.CharField(max_length=255, blank=True, null=True, verbose_name='Upozila or Thana')
    pourashava = models.CharField(max_length=255, blank=True, null=True, verbose_name='Pourashava or City Corporation')
    union_parishad = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    mouza = models.CharField(max_length=255, blank=True, null=True)
    village = models.TextField(max_length=555, blank=True, null=True, verbose_name='Rasta/village')
    house_holding_number = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'School Address Information'

    def __str__(self):
        return self.school_address.name




class SchoolContactInformation(UniversalModel):
    school_contact = models.ForeignKey(WebsiteInformation, on_delete=models.DO_NOTHING, related_name='school_contact_information')
    school_contact_address = models.ForeignKey(SchoolAddressInformation, on_delete=models.DO_NOTHING, related_name='school_contact_address')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Phone Number')
    email = models.EmailField(blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_contact_slug, unique=True, null=False, db_index=True)

    class Meta:
        verbose_name_plural = 'School Contact Information'

    def __str__(self):
        return self.school_contact.name 
    


class WebsiteHomeSliderContent(UniversalModel):
    website_home_slider_content = models.ForeignKey(WebsiteInformation, on_delete=models.DO_NOTHING, related_name='school_website_slider_information')
    slug = AutoSlugField(populate_from=get_website_home_slider_content_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    title = models.CharField(max_length=30,
                            db_index=True,
                            verbose_name='Title')
    description = models.TextField(max_length=100,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    
    class Meta:
        verbose_name_plural = 'School Website Home Slider Content'
    
    def __str__(self):
        return self.title 



class WebsiteHomeSliderContentFile(UniversalModel):
    home_content = models.ForeignKey(
        WebsiteHomeSliderContent,
        on_delete=models.DO_NOTHING,
        related_name='home_content_info')
    image = VersatileImageField(
        upload_to=get_website_home_slider_content_image,
        null=True, blank=True)
    slug = AutoSlugField(populate_from=get_website_home_slider_content_file_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    
    class Meta:
        verbose_name_plural = 'School Website Home Slider Content File'



class  WebsiteAbout(UniversalModel):
    website_about_content =  models.ForeignKey(WebsiteInformation, on_delete=models.DO_NOTHING, related_name='school_website_about_information')
    title = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    
    short_description = models.TextField(max_length=1000, validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   verbose_name="School Short Description"
                                   )
    long_description = models.TextField(max_length=2000, validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   verbose_name="School Long Description"
                                   )
    
    start_year = models.DateField()
    years_of_experience = models.CharField(max_length=200, blank=True, null=True)

    vision = models.TextField(max_length=1000, blank=True, null=True, verbose_name="School Vision")
    mission = models.TextField(max_length=1000, blank=True, null=True, verbose_name="School Mission")
    slug = AutoSlugField(populate_from=get_website_about_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    
    class Meta:
        verbose_name_plural = 'School Website About'


    def __str__(self):
        return self.title 


    def save(self, *args, **kwargs):
        import datetime
        import dateutil
        import dateutil.relativedelta
        now = datetime.datetime.utcnow()
        now = now.date()
        age = dateutil.relativedelta.relativedelta(now, self.start_year)
        experience = age.years
        self.years_of_experience = experience
        super().save(*args, **kwargs)




class  WebsiteAboutFile(UniversalModel):
    about = models.ForeignKey(WebsiteAbout, on_delete=models.DO_NOTHING, related_name='website_about_file_content')
    slug = AutoSlugField(populate_from=get_website_about_file_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    image = VersatileImageField(
        upload_to=get_website_about_file_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'School Website About File'
    
    def __str__(self):
        return self.about.title 

    


# # # def create_website_about_file_content(sender, instance, created, **kwargs):

# # #     if created:
# # #         WebsiteAboutFile.objects.create(
# # #             about=instance)


# # # post_save.connect(create_website_about_file_content, sender=WebsiteAbout)




class WebsiteFunFactContent(UniversalModel):
    about_info = models.ForeignKey(WebsiteAbout,
                              on_delete=models.DO_NOTHING,
                              blank=True, null=True,
                              related_name="about_fun_fact_content")
    years_of_experience = models.CharField(max_length=20, blank=True, null=True)
    number_of_students = models.CharField(max_length=50, blank=True, null=True)
    number_of_alumni = models.CharField(max_length=50, blank=True, null=True)
    winning_awards = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'School Website Fun Fact Content'

    def __str__(self):
        return self.about_info.title 


    def save(self, *args, **kwargs):
        self.years_of_experience = self.about_info.years_of_experience
        super().save(*args, **kwargs)



# # # def create_fun_fact_content(sender, instance, created, **kwargs):

# # #     if created:
# # #         WebsiteFunFactContent.objects.create(
# # #             about_info=instance)


# # # post_save.connect(create_fun_fact_content, sender=WebsiteAbout)

class WebsiteAboutWinningAwards(UniversalModel):
    school_award = models.ForeignKey(WebsiteAbout,on_delete=models.DO_NOTHING,
                              blank=True, null=True,
                              related_name='school_award_process')
    title = models.CharField(max_length=200, blank=True, null=True)
    awards_image = VersatileImageField(
        upload_to=get_website_about_file_awards_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'School Website About Winning Awards'
    
    def __str__(self):
        return self.school_award.title 


class SchoolAdmission(UniversalModel):
    school_admission = models.ForeignKey(WebsiteInformation, on_delete=models.DO_NOTHING,
                              blank=True, null=True,
                              related_name='school_admission_process')
    title = models.TextField(max_length=500, blank=True, null=True)
    admission_class = models.CharField(max_length=20, choices=AdmissionClass.choices, blank=True, null=True, verbose_name='Admission Class')
    admission_branch = models.CharField(max_length=20, choices=AdmissionBranch.choices, blank=True, null=True, verbose_name='Admission Branch')
    admission_division = models.CharField(max_length=20, choices=AdmissionDivision.choices, blank=True, null=True, verbose_name='Admission Division')
    number_of_seats = models.CharField(max_length=100, blank=True, null=True)
    limit_of_age = models.CharField(max_length=100, blank=True, null=True)
    collection_of_prospectus = models.TextField(max_length=1000, blank=True, null=True)
    fill_the_application_form = models.TextField(max_length=1000, blank=True, null=True)
    online_admission_form_date_time = models.TextField(max_length=1000, blank=True, null=True)
    admission_process_college_information_website = models.URLField(blank=True, null=True)
    digital_lottery_time_information = models.TextField(max_length=1000, blank=True, null=True)
    admission_application_rules = models.TextField(max_length=1000, blank=True, null=True)
    other_description = models.TextField(max_length=1000, blank=True, null=True)
    remark = models.TextField(max_length=1000, blank=True, null=True)
    pdf_file = models.FileField(upload_to=get_website_school_admission_pdf, blank=True, null=True, verbose_name='PDF File')
    slug = AutoSlugField(populate_from=get_website_school_admission_slug, unique=True,null=True,db_index=True)

    class Meta:
        verbose_name_plural = 'School Admission Process'

    def __str__(self):
        return self.title



class AcademicInformation(UniversalModel):
    school_academic_information = models.OneToOneField(WebsiteInformation, on_delete=models.CASCADE, related_name='school_academic_information')
    title = models.TextField(max_length=500, blank=True, null=True)
    code_of_conducts = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Code of Conducts')
    guideline_for_parents = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Guideline for Parents')
    dress_code = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Dress Code')
    homework_and_lecture_documents = models.FileField(upload_to=get_website_school_academic_homework_and_lecture_documents_pdf, null=True, blank=True, verbose_name='Homework and Class Lecture Documents')
    lesson_plan = models.FileField(upload_to=get_website_school_academic_lesson_plan_documents_pdf, null=True, blank=True, verbose_name='Lesson Plan')
    academic_calendar = models.FileField(upload_to=get_website_school_academic_calendar_documents_pdf, null=True, blank=True, verbose_name='Academic Calendar')
    syllabus = models.FileField(upload_to=get_website_school_academic_syllabus_documents_pdf, null=True, blank=True, verbose_name='Syllabus')
    class_routine = models.FileField(upload_to=get_website_school_academic_class_routine_documents_pdf, null=True, blank=True, verbose_name='Class Routine')
    co_curricular_activities = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Co-curricular Activities')
    slug = AutoSlugField(populate_from=get_website_school_academic_slug, unique=True,null=True,db_index=True)

    class Meta:
        verbose_name_plural = 'School Academic Information'

    def __str__(self):
        return f"Academic Information for {self.school_academic_information.name}"




class WebSiteGalleryInformation(UniversalModel):
    school_website_gallery =  models.OneToOneField(WebsiteInformation, on_delete=models.CASCADE, related_name='school_website_gallery_information')
    image = VersatileImageField(
        upload_to=get_website_get_gallery_image,
        null=True, blank=True,
        verbose_name='Image'
    )

    class Meta:
        verbose_name_plural = 'School Website Gallery Images'
        ordering = ['-createdAt']  

    def __str__(self):
        return f"Gallery Image for {self.school_website_gallery.name}"
    



class NewsEvents(UniversalModel):
    school_website_news_events =  models.OneToOneField(WebsiteInformation, on_delete=models.DO_NOTHING, related_name='school_website_news_events_information')
    news_events_status = models.CharField(
        max_length=100,
        choices=NewsEventsStatus.choices,
        db_index=True,
        default=NewsEventsStatus.NEWS,
        verbose_name='Type'
    )
    slug = AutoSlugField(populate_from=get_news_events_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    headline = models.CharField(max_length=300,
                                blank=True,
                                null=True,
                                db_index=True,
                                verbose_name='Title')
    description = models.TextField(max_length=None,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    publish_date = models.DateTimeField(blank=True, null=True)

    image = VersatileImageField(
        upload_to=get_news_events_image,
        null=True, blank=True)
    
    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = 'News and Events'

    def __str__(self):
        return self.headline 