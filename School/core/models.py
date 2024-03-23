from tokenize import blank_re
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from school_auth.models import User

from common.models import SchoolInformationOnBoarding
from common.models import BaseModel, SchoolInformationOnBoarding

from .utills import (
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
    get_news_events_image,
    get_blog_slug,
    get_social_media_slug,
    get_alumni_section_slug,
    get_website_teacher_slug,
    get_website_managing_committee_member_slug,
    get_website_staff_slug,
    get_website_faculty_slug,
    get_blog_image,
    get_blog_image_slug,
    get_testimonials_image,
    get_testimonials_slug,
    get_alumni_section_slug,
    get_alumni_section_image_slug
)

from .choice import (
    Status,
    AdmissionClass,
    AdmissionBranch,
    AdmissionDivision,
    NewsEventsStatus,
    AttendanceType,
)


class UniversalModel(BaseModel):
    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.Active
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="User_who_created",
        verbose_name="Created Person",
    )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="The_User_who_Updated",
        verbose_name="Updated Person",
    )


class SchoolClass(UniversalModel):
    school_info = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="School_Class_Information",
    )
    class_teacher = models.ForeignKey(
        "TeacherApp.Teacher",
        on_delete=models.DO_NOTHING,
        related_name="class_teachers",
        blank=True, null=True,
        db_index=True,
    )
    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from=get_school_class_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    total_students = models.PositiveIntegerField(default=0)
    present_students = models.PositiveIntegerField(default=0)
    absent_students = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "School Class"

    def __str__(self):
        return self.name


class SchoolSection(UniversalModel):
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.DO_NOTHING, related_name="school_class_section"
    )
    name = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from=get_school_section_slug, unique=True, null=False, db_index=True
    )

    class Meta:
        verbose_name_plural = "School Class Section"

    def __str__(self):
        return self.name


class WebsiteInformation(UniversalModel):
    school_website = models.OneToOneField(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_website_information",
    )
    name = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    logo = VersatileImageField(upload_to=get_school_website_logo, null=True, blank=True)
    favicon = VersatileImageField(
        upload_to=get_school_website_favicon, null=True, blank=True
    )
    slug = AutoSlugField(
        populate_from=get_school_website_slug, unique=True, null=False, db_index=True
    )
    school_address = models.ForeignKey(
        "core.SchoolAddressInformation",
        on_delete=models.DO_NOTHING,
        related_name="school_address_information",
        blank=True,
        null=True,
    )
    school_contact = models.ForeignKey(
        "core.SchoolContactInformation",
        on_delete=models.DO_NOTHING,
        related_name="school_contact_information",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "School Website Information"
        indexes = [
            models.Index(fields=["school_website"]),
        ]

    def __str__(self):
        return self.name


class SchoolAddressInformation(UniversalModel):
    school_address = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_address_information",
    )
    slug = AutoSlugField(
        populate_from=get_school_address_slug, unique=True, null=False, db_index=True
    )
    divisions = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    upazila = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Upozila or Thana"
    )
    pourashava = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Pourashava or City Corporation",
    )
    union_parishad = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    mouza = models.CharField(max_length=255, blank=True, null=True)
    village = models.TextField(
        max_length=555, blank=True, null=True, verbose_name="Rasta/village"
    )
    house_holding_number = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "School Address Information"
        indexes = [
            models.Index(fields=["school_address"]),
        ]

    def __str__(self):
        return self.school_address.name


class SchoolContactInformation(UniversalModel):
    school_contact = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_contact_information",
    )
    school_contact_address = models.ForeignKey(
        SchoolAddressInformation,
        on_delete=models.DO_NOTHING,
        related_name="school_contact_address",
    )
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
    email = models.EmailField(blank=True, null=True)
    slug = AutoSlugField(
        populate_from=get_school_contact_slug, unique=True, null=False, db_index=True
    )

    class Meta:
        verbose_name_plural = "School Contact Information"
        indexes = [
            models.Index(fields=["school_contact"]),
            models.Index(fields=["school_contact_address"]),
        ]

    def __str__(self):
        return self.school_contact.name


class WebsiteHomeSliderContent(UniversalModel):
    website_home_slider_content = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_website_slider_information",
    )
    slug = AutoSlugField(
        populate_from=get_website_home_slider_content_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    title = models.CharField(max_length=30, db_index=True, verbose_name="Title")
    description = models.TextField(
        max_length=100,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "School Website Home Slider Content"

    def __str__(self):
        return self.title


class WebsiteHomeSliderContentFile(UniversalModel):
    home_content = models.ForeignKey(
        WebsiteHomeSliderContent,
        on_delete=models.DO_NOTHING,
        related_name="home_content_info",
    )
    image = VersatileImageField(
        upload_to=get_website_home_slider_content_image, null=True, blank=True
    )
    slug = AutoSlugField(
        populate_from=get_website_home_slider_content_file_slug,
        unique=True,
        null=True,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = "School Website Home Slider Content File"


class WebsiteAbout(UniversalModel):
    website_about_content = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_website_about_information",
    )
    title = models.CharField(max_length=200, db_index=True, verbose_name="Title")

    short_description = models.TextField(
        max_length=1000,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        verbose_name="School Short Description",
    )
    long_description = models.TextField(
        max_length=2000,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        verbose_name="School Long Description",
    )

    start_year = models.DateField()
    years_of_experience = models.CharField(max_length=200, blank=True, null=True)

    vision = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="School Vision"
    )
    mission = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="School Mission"
    )
    slug = AutoSlugField(
        populate_from=get_website_about_slug, unique=True, null=True, db_index=True
    )

    class Meta:
        verbose_name_plural = "School Website About"

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


class WebsiteAboutFile(UniversalModel):
    about = models.ForeignKey(
        WebsiteAbout,
        on_delete=models.DO_NOTHING,
        related_name="website_about_file_content",
    )
    slug = AutoSlugField(
        populate_from=get_website_about_file_slug, unique=True, null=True, db_index=True
    )
    image = VersatileImageField(
        upload_to=get_website_about_file_image, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "School Website About File"

    def __str__(self):
        return self.about.title


class WebsiteFunFactContent(UniversalModel):
    about_info = models.ForeignKey(
        WebsiteAbout,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="about_fun_fact_content",
    )
    years_of_experience = models.CharField(max_length=20, blank=True, null=True)
    number_of_students = models.CharField(max_length=50, blank=True, null=True)
    number_of_alumni = models.CharField(max_length=50, blank=True, null=True)
    winning_awards = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "School Website Fun Fact Content"

    def __str__(self):
        return self.about_info.title

    def save(self, *args, **kwargs):
        self.years_of_experience = self.about_info.years_of_experience
        super().save(*args, **kwargs)


class WebsiteAboutWinningAwards(UniversalModel):
    school_award = models.ForeignKey(
        WebsiteAbout,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="school_award_process",
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    awards_image = VersatileImageField(
        upload_to=get_website_about_file_awards_image, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "School Website About Winning Awards"

    def __str__(self):
        return self.school_award.title


class SchoolAdmission(UniversalModel):
    school_admission = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="school_admission_process",
    )
    title = models.TextField(max_length=500, blank=True, null=True)
    admission_class = models.CharField(
        max_length=20,
        choices=AdmissionClass.choices,
        blank=True,
        null=True,
        verbose_name="Admission Class",
    )
    admission_branch = models.CharField(
        max_length=20,
        choices=AdmissionBranch.choices,
        blank=True,
        null=True,
        verbose_name="Admission Branch",
    )
    admission_division = models.CharField(
        max_length=20,
        choices=AdmissionDivision.choices,
        blank=True,
        null=True,
        verbose_name="Admission Division",
    )
    number_of_seats = models.CharField(max_length=100, blank=True, null=True)
    limit_of_age = models.CharField(max_length=100, blank=True, null=True)
    collection_of_prospectus = models.TextField(max_length=1000, blank=True, null=True)
    fill_the_application_form = models.TextField(max_length=1000, blank=True, null=True)
    online_admission_form_date_time = models.TextField(
        max_length=1000, blank=True, null=True
    )
    admission_process_college_information_website = models.URLField(
        blank=True, null=True
    )
    digital_lottery_time_information = models.TextField(
        max_length=1000, blank=True, null=True
    )
    admission_application_rules = models.TextField(
        max_length=1000, blank=True, null=True
    )
    other_description = models.TextField(max_length=1000, blank=True, null=True)
    remark = models.TextField(max_length=1000, blank=True, null=True)
    pdf_file = models.FileField(
        upload_to=get_website_school_admission_pdf,
        blank=True,
        null=True,
        verbose_name="PDF File",
    )
    slug = AutoSlugField(
        populate_from=get_website_school_admission_slug,
        unique=True,
        null=True,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = "School Admission Process"

    def __str__(self):
        return self.title


class AcademicInformation(UniversalModel):
    school_academic_information = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.CASCADE,
        related_name="school_academic_information",
    )

    title = models.TextField(max_length=500, blank=True, null=True)
    code_of_conducts = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Code of Conducts",
    )
    guideline_for_parents = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Guideline for Parents",
    )
    dress_code = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Dress Code",
    )
    homework_and_lecture_documents = models.FileField(
        upload_to=get_website_school_academic_homework_and_lecture_documents_pdf,
        null=True,
        blank=True,
        verbose_name="Homework and Class Lecture Documents",
    )
    lesson_plan = models.FileField(
        upload_to=get_website_school_academic_lesson_plan_documents_pdf,
        null=True,
        blank=True,
        verbose_name="Lesson Plan",
    )
    academic_calendar = models.FileField(
        upload_to=get_website_school_academic_calendar_documents_pdf,
        null=True,
        blank=True,
        verbose_name="Academic Calendar",
    )
    syllabus = models.FileField(
        upload_to=get_website_school_academic_syllabus_documents_pdf,
        null=True,
        blank=True,
        verbose_name="Syllabus",
    )
    class_routine = models.FileField(
        upload_to=get_website_school_academic_class_routine_documents_pdf,
        null=True,
        blank=True,
        verbose_name="Class Routine",
    )
    co_curricular_activities = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="Co-curricular Activities"
    )
    slug = AutoSlugField(
        populate_from=get_website_school_academic_slug,
        unique=True,
        null=True,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = "School Academic Information"

    def __str__(self):
        return f"Academic Information for {self.school_academic_information.name}"


class WebSiteGalleryInformation(UniversalModel):
    school_website_gallery = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.CASCADE,
        related_name="school_website_gallery_information",
    )
    image = VersatileImageField(
        upload_to=get_website_get_gallery_image,
        null=True,
        blank=True,
        verbose_name="Image",
    )

    class Meta:
        verbose_name_plural = "School Website Gallery Images"
        ordering = ["-createdAt"]

    def __str__(self):
        return f"Gallery Image for {self.school_website_gallery}"


class NewsEvents(UniversalModel):
    school = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="news_schools",
    )
    news_events_status = models.CharField(
        max_length=100,
        choices=NewsEventsStatus.choices,
        db_index=True,
        default=NewsEventsStatus.NEWS,
        verbose_name="Type",
    )
    slug = AutoSlugField(
        populate_from=get_news_events_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    headline = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Title",
    )
    description = models.TextField(
        max_length=None,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
    )
    publish_date = models.DateTimeField(blank=True, null=True)

    image = VersatileImageField(
        upload_to=get_news_events_image,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-publish_date"]
        verbose_name_plural = "News and Events"

    def __str__(self):
        return self.headline


class BlogCategory(UniversalModel):
    name = models.CharField(max_length=100, unique=True)
    school_blog_category = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="blog_categories",
        verbose_name="School Blog Category",
    )

    def __str__(self):
        return self.name


class BlogTag(UniversalModel):
    name = models.CharField(max_length=100, unique=True)
    school_blog_tag = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="blog_tags",
        verbose_name="School Blog Tag",
    )

    def __str__(self):
        return self.name


class Blog(UniversalModel):
    school_blog = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="school_website_blog_information",
        verbose_name="School Website Blog Information",
    )
    slug = AutoSlugField(
        populate_from=get_blog_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    title = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Title",
    )
    content = models.TextField(
        max_length=None,
        blank=True,
        null=True,
        verbose_name="Content",
    )
    publish_date = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(
        BlogCategory,
        blank=True,
        verbose_name="Categories",
    )
    tags = models.ManyToManyField(
        BlogTag,
        blank=True,
        verbose_name="Tags",
    )

    class Meta:
        ordering = ["-publish_date"]
        verbose_name_plural = "School Blog Posts"

    def __str__(self):
        return self.title


class BlogImage(UniversalModel):
    blog_info = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="blog_image_information"
    )
    slug = AutoSlugField(
        populate_from=get_blog_image_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    image = VersatileImageField(
        upload_to=get_blog_image,
        null=True,
        blank=True,
    )


class SocialMedia(UniversalModel):
    school_social_media = models.OneToOneField(
        SchoolInformationOnBoarding,
        on_delete=models.CASCADE,
        related_name="social_media_info",
        verbose_name="SocialMedia Website Information",
    )
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook URL")
    twitter_url = models.URLField(blank=True, null=True, verbose_name="Twitter URL")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram URL")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn URL")
    slug = AutoSlugField(
        populate_from=get_social_media_slug, unique=True, null=True, db_index=True
    )

    class Meta:
        verbose_name_plural = "Social Media Information"

    def __str__(self):
        return f"Social Media Information for {self.school_social_media_website_information.name}"


class AlumniSection(UniversalModel):
    school_alumni_section = models.OneToOneField(
        SchoolInformationOnBoarding,
        on_delete=models.CASCADE,
        related_name="alumni_section_info",
        verbose_name="School Website Alumni Information",
    )
    slug = AutoSlugField(
        populate_from=get_alumni_section_slug, unique=True, null=True, db_index=True
    )
    about_alumni = models.TextField(blank=True, null=True, verbose_name="About Alumni")
    alumni_events = models.TextField(
        blank=True, null=True, verbose_name="Alumni Events"
    )
    alumni_news = models.TextField(blank=True, null=True, verbose_name="Alumni News")

    class Meta:
        verbose_name_plural = "Alumni Section Information"

    def __str__(self):
        return f"Alumni Section Information for {self.school_alumni_section_website_information.name}"


class AlumniSectionImage(UniversalModel):
    alumni_info = models.ForeignKey(
        AlumniSection, on_delete=models.CASCADE, related_name="alumni_section_images"
    )
    slug = AutoSlugField(
        populate_from=get_alumni_section_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    image = VersatileImageField(
        upload_to=get_alumni_section_image_slug,
        null=True,
        blank=True,
    )


class WebsiteTeacherInformation(UniversalModel):
    school_teacher = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="teachers",
        verbose_name="School Website Teacher Information",
    )
    slug = AutoSlugField(
        populate_from=get_website_teacher_slug, unique=True, null=True, db_index=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, verbose_name="Position")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    contact_email = models.EmailField(
        blank=True, null=True, verbose_name="Contact Email"
    )
    contact_phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Contact Phone"
    )

    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class WebsiteManagingCommitteeMemberInformation(UniversalModel):
    school_managing_committee_member = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="ManagingCommitteeMember",
        verbose_name="School Website ManagingCommitteeMember Information",
    )
    slug = AutoSlugField(
        populate_from=get_website_managing_committee_member_slug,
        unique=True,
        null=True,
        db_index=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, verbose_name="Position")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    contact_email = models.EmailField(
        blank=True, null=True, verbose_name="Contact Email"
    )
    contact_phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Contact Phone"
    )

    class Meta:
        verbose_name_plural = "ManagingCommitteeMember"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class WebsiteStaffInformation(UniversalModel):
    school_staff = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="staff",
        verbose_name="School Website Staff Information",
    )
    slug = AutoSlugField(
        populate_from=get_website_staff_slug, unique=True, null=True, db_index=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, verbose_name="Position")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    contact_email = models.EmailField(
        blank=True, null=True, verbose_name="Contact Email"
    )
    contact_phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Contact Phone"
    )

    class Meta:
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class WebSiteFacultyInformation(UniversalModel):
    school_faculty = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="faculty_members",
        verbose_name="School Faculty Website Information",
    )
    slug = AutoSlugField(
        populate_from=get_website_faculty_slug, unique=True, null=True, db_index=True
    )
    teachers = models.ManyToManyField(
        WebsiteTeacherInformation,
        blank=True,
        related_name="faculty_membership",
        verbose_name="Teachers",
    )
    staff_members = models.ManyToManyField(
        WebsiteStaffInformation,
        blank=True,
        related_name="faculty_membership",
        verbose_name="Staff Members",
    )
    managing_committee_member = models.ManyToManyField(
        WebsiteManagingCommitteeMemberInformation,
        blank=True,
        related_name="Managing_Committee_Member_Information",
    )

    class Meta:
        verbose_name_plural = "Faculty Members"

    def __str__(self):
        return f"Faculty Members for {self.school_faculty_website_information.name}"


class Testimonials(BaseModel):
    school_testimonials = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="Testimonials",
        verbose_name="Testimonials",
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.TextField(max_length=None, blank=True, null=True)
    comment = models.TextField(max_length=None, blank=True, null=True)
    image = VersatileImageField(upload_to=get_testimonials_image, null=True, blank=True)
    slug = AutoSlugField(
        populate_from=get_testimonials_slug, unique=True, null=True, db_index=True
    )

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"


class ClassAttendance(UniversalModel):
    # foreign_key fields for ClassAttendance
    attendance_class = models.ForeignKey(
        "core.SchoolClass",
        on_delete=models.DO_NOTHING,
        related_name="class_attendances",
        db_index=True,
    )
    attendance_section = models.ForeignKey(
        "core.SchoolSection",
        on_delete=models.DO_NOTHING,
        related_name="section_attendances",
        db_index=True,
        blank=True,
        null=True,
    )

    attendance_student = models.ForeignKey(
        "StudentApp.Student",
        on_delete=models.DO_NOTHING,
        related_name="attendant_students",
        db_index=True,
    )
    school = models.ForeignKey(
        "common.SchoolInformationOnBoarding",
        on_delete=models.DO_NOTHING,
        related_name="school_attendances",
        db_index=True,
        blank=True,
        null=True,
    )
    marked_by = models.ForeignKey(
        "school_auth.User",
        on_delete=models.SET_NULL,
        related_name="marked_attendances",
        null=True,
        blank=True,
    )

    # model fields
    is_present = models.BooleanField(default=False)
    on_leave = models.BooleanField(default=True)
    date = models.DateTimeField()
    late_arrival = models.BooleanField(default=False)
    early_departure = models.BooleanField(default=False)
    leave_reason = models.CharField(max_length=255, blank=True)
    attendance_type = models.CharField(
        max_length=20,
        choices=AttendanceType,
        default=AttendanceType.STUDENT,
    )
    comments = models.TextField(blank=True)
