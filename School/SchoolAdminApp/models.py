from django.db import models
from django.db.models import Sum
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from common.models import  SchoolInformationOnBoarding
from school_auth.models import User

from core.models import (
    UniversalModel,
    SchoolClass, 
    SchoolSection)

from StudentApp.models import(
    Student
)


from .choice import (
    Gender,
    JobType,
    JobStatus,
    BookType,
    BookStatus,
    HostelRoomType,
    HostelAvailability,
    PurchaseRequestStatus,
    PurchaseReceivedStatus,
    HolidayType
)

from .utills import(
    get_school_admin_slug,
    get_school_admin_image_slug,
    get_admin_profile_image,
    get_school_career_slug,
    get_school_library_slug,
    get_school_transport_slug,
    get_school_vendor_slug,
    get_school_product_category_slug,
    get_school_product_slug,
    get_school_purchase_request_slug,
    get_school_purchase_received_slug,
    get_school_class_time_table_slug,
    get_school_exam_slug,
    get_school_hostel_slug,
    get_school_sports_slug,
    get_school_grading_slug,
    get_school_semester_slug,
    get_school_holiday_slug
)


class SchoolAdmin(UniversalModel):
    school_admin = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_admin_information')
    schoolUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_school_admin_info')
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        blank=True, null=True
    )
    date_Of_birth = models.DateField(blank=True, null=True)
    phone =  PhoneNumberField(blank=True, null=True, verbose_name='Phone Number')
    joining_date  = models.DateTimeField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_admin_slug, unique=True, null=False, db_index=True)

   
    def __str__(self):
        return self.schoolUser.username
    
    

class SchoolAdminImage(UniversalModel):
    school_admin_info = models.ForeignKey(SchoolAdmin, on_delete=models.DO_NOTHING, related_name='school_admin_information')
    slug = AutoSlugField(populate_from=get_school_admin_image_slug, unique=True, null=False, db_index=True)
    image = VersatileImageField(upload_to=get_admin_profile_image, null=True, blank=True)




class Department(UniversalModel):
    school_department = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_departments')
    department_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=500, blank=True, null=True)
    head_of_department = models.CharField(max_length=500, blank=True, null=True)



class Subject(UniversalModel):
    school_subject = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_subject_information')
    class_subject = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='class_subject_information')
    subject_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Career(UniversalModel):
    school_career = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_job_circular')
    career_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="job_department")
    title = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=550, blank=True, null=True)
    experience = models.TextField(max_length=1000, blank=True, null=True)
    no_of_vacancies = models.CharField(max_length=100, blank=True, null=True)
    age_limit = models.CharField(max_length=100, blank=True, null=True)
    salary_from = models.CharField(max_length=255, blank=True, null=True)
    salary_to = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(
        max_length=50,
        choices=JobType.choices,
        blank=True, null=True
    )
    job_status = models.CharField(
        max_length=30,
        choices=JobStatus.choices,
        blank=True, null=True
    )
    start_date = models.DateTimeField(blank=True, null=True)
    expired_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_career_slug, unique=True, null=False, db_index=True)

    class Meta:
        ordering = ["-createdAt"]
        verbose_name_plural = "Career"



class Library(UniversalModel):
    school_library = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_libraries')
    library_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="library_departments")
    library_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="library_classes")
    slug = AutoSlugField(populate_from=get_school_library_slug, unique=True, null=False, db_index=True)
    book_id = models.CharField(max_length=100, unique=False)
    book_name = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    book_type = models.CharField(
        max_length=30,
        choices=BookType.choices,
        blank=True, null=True
    )
    book_status = models.CharField(
        max_length=30,
        choices=BookStatus.choices,
        blank=True, null=True
    )
    


class Transport(UniversalModel):
    school_transport = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_transports')
    slug = AutoSlugField(populate_from=get_school_transport_slug, unique=True, null=False, db_index=True)
    route_name =  models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    driver_name = models.CharField(max_length=500, blank=True, null=True)
    license_number = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=500, blank=True, null=True)
    driver_address = models.TextField(blank=True, null=True)



class Hostel(UniversalModel):
    school_hostel = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_hostel')
    block = models.CharField(max_length=255, blank=True, null=True)
    room_number = models.CharField(max_length=255, blank=True, null=True)
    room_type = models.CharField(
        max_length=30,
        choices=HostelRoomType.choices,
        blank=True, null=True
    )
    number_of_beds = models.CharField(max_length=100, blank=True, null=True)
    cose_per_bed = models.CharField(max_length=100, blank=True, null=True)
    availability = models.CharField(
        max_length=30,
        choices=HostelAvailability.choices,
        blank=True, null=True
    )
    slug = AutoSlugField(populate_from=get_school_hostel_slug, unique=True, null=False, db_index=True)


class SportsInformation(UniversalModel):
    school_sports = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_sports')
    sports_id = models.CharField(max_length=100, unique=False)
    sports_name = models.CharField(max_length=255, blank=True, null=True)
    coach_name = models.CharField(max_length=255, blank=True, null=True)
    started_year = models.CharField(max_length=255, blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_sports_slug, unique=True, null=False, db_index=True)



class ClassTimeTable(UniversalModel):
    school_class_time_table = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_class_time_table')
    school_time_table = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_class_information')
    school_section_time_table = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_section_information')
    teacher_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    class_date = models.DateTimeField(blank=True, null=True)
    class_start_time = models.TimeField(blank=True, null=True)
    class_end_time = models.TimeField(blank=True, null=True)
    class_time_table_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_class_time_table_subjects')
    slug = AutoSlugField(populate_from=get_school_class_time_table_slug, unique=True, null=False, db_index=True)


class Exam(UniversalModel):
    school_exam = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_exams')
    exam_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='exam_classes')
    exam_section = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='exam_sections')
    name = models.CharField(max_length=255, blank=True, null=True)
    fees = models.CharField(max_length=255, blank=True, null=True)
    exam_start_time = models.TimeField(blank=True, null=True)
    exam_end_time = models.TimeField(blank=True, null=True)
    exam_date = models.DateTimeField(blank=True, null=True)
    exam_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_exam_subjects')
    slug = AutoSlugField(populate_from=get_school_exam_slug, unique=True, null=False, db_index=True)




class Vendor(UniversalModel):
    school_vendor = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_vendors')
    slug = AutoSlugField(populate_from=get_school_vendor_slug, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name='Phone Number')

    def __str__(self):
        return self.name



class ProductCategory(UniversalModel):
    school_product_category = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_product_categories')
    slug = AutoSlugField(populate_from=get_school_product_category_slug, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Product(UniversalModel):
    school_product = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_products')
    category = models.ForeignKey(
        ProductCategory, 
        on_delete=models.DO_NOTHING,
        blank=True, 
        null=True, 
        related_name='school_product_categories_info')
    slug = AutoSlugField(populate_from=get_school_product_slug, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name



class PurchaseRequest(UniversalModel):
    school_purchase_request = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_purchases_request')
    purchase_request_vendor = models.ForeignKey(
        Vendor,
        on_delete=models.DO_NOTHING, 
        blank=True, 
        null=True,
        related_name='purchase_request_vendors')
    purchase_request_status = models.CharField(
        max_length=30,
        choices=PurchaseRequestStatus.choices
    )
    slug = AutoSlugField(populate_from=get_school_purchase_request_slug, unique=True, null=False, db_index=True)
    product_request = models.ManyToManyField(Product, related_name='product_requests')
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)




class PurchaseReceived(UniversalModel):
    school_purchase_received = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_purchases_received')
    purchase_received_vendor = models.ForeignKey(
        Vendor,
        on_delete=models.DO_NOTHING, 
        blank=True, 
        null=True,
        related_name='purchase_received_vendors')
    purchase_request = models.ForeignKey(
        PurchaseRequest,
        on_delete=models.DO_NOTHING, 
        blank=True, 
        null=True,
        related_name='purchase_requests')
    purchase_received_status = models.CharField(
        max_length=30,
        choices=PurchaseReceivedStatus.choices
    )
    slug = AutoSlugField(populate_from=get_school_purchase_received_slug, unique=True, null=False, db_index=True)
    product = models.ManyToManyField(Product, related_name='product_received')
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    partially_received = models.PositiveIntegerField(blank=True, null=True)
    all_received = models.PositiveIntegerField(blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    note_private = models.TextField(blank=True, null=True)
    note_public = models.TextField(blank=True, null=True)



class GradingConfig(UniversalModel):
    school_grading = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_grading_info')
    slug = AutoSlugField(populate_from=get_school_grading_slug, unique=True, null=False, db_index=True)
    letter_grade_A_plus =  models.CharField(max_length=100, help_text = "A+")
    letter_grade_A =  models.CharField(max_length=100, help_text = "A")
    letter_grade_A_minus = models.CharField(max_length=100, help_text = "A-")
    letter_grade_B = models.CharField(max_length=100, help_text = "B")
    letter_grade_C = models.CharField(max_length=100, help_text = "C")
    letter_grade_D = models.CharField(max_length=100, help_text = "D")
    letter_grade_F = models.CharField(max_length=100, help_text = "F")

    def __str__(self):
        return self.school_grading.name
    

class Semester(UniversalModel):
    school_semester = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_semester_info')
    slug = AutoSlugField(populate_from=get_school_semester_slug, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=100, help_text = "Title")
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Result(UniversalModel):
    school_result = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_result')
    result_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='result_classes')
    result_section = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='result_sections')
    result_semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='result_semester')
    result_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='result_subject')
    result_student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='result_students')
    mark = models.IntegerField(help_text="Mark")

    def __str__(self):
        return self.mark
    
    def count_subjects(self):
        return self.result_subject.count()

    def count_total_marks(self):
        total_marks = 0
        for subject_result in self.result_subject.all():
            if subject_result.mark:  
                total_marks += subject_result.mark
        return total_marks

    def average_marks(self):
        total_marks = 0
        total_subjects = 0
        for subject_result in self.result_subject.all():
            if subject_result.mark is not None:
                total_marks += subject_result.mark
                total_subjects += 1

        return total_marks / total_subjects if total_subjects > 0 else 0
    
    def total_marks_for_student(self, student):
        return Result.objects.filter(result_student=student).aggregate(total_marks=Sum('mark'))['total_marks'] or 0

    def average_marks_for_student(self, student):
        total_marks = Result.objects.filter(result_student=student).aggregate(total_marks=Sum('mark'))['total_marks'] or 0
        total_subjects = Result.objects.filter(result_student=student).count()
        return total_marks / total_subjects if total_subjects > 0 else 0

    def total_marks_for_subject(self, subject):
        return Result.objects.filter(result_subject=subject).aggregate(total_marks=Sum('mark'))['total_marks'] or 0

    def average_marks_for_subject(self, subject):
        total_marks = Result.objects.filter(result_subject=subject).aggregate(total_marks=Sum('mark'))['total_marks'] or 0
        total_students = Result.objects.filter(result_subject=subject).count()
        return total_marks / total_students if total_students > 0 else 0

    def total_marks_for_class(self, school_class):
        return Result.objects.filter(result_class=school_class).aggregate(total_marks=Sum('mark'))['total_marks'] or 0

    def average_marks_for_class(self, school_class):
        total_marks = Result.objects.filter(result_class=school_class).aggregate(total_marks=Sum('mark'))['total_marks'] or 0
        total_students = Result.objects.filter(result_class=school_class).count()
        return total_marks / total_students if total_students > 0 else 0

    def total_marks_for_section(self, section):
        return Result.objects.filter(result_section=section).aggregate(total_marks=Sum('mark'))['total_marks'] or 0

    def average_marks_for_section(self, section):
        total_marks = Result.objects.filter(result_section=section).aggregate(total_marks=Sum('mark'))['total_marks'] or 0
        total_students = Result.objects.filter(result_section=section).count()
        return total_marks / total_students if total_students > 0 else 0


class StudentSubjectResult(UniversalModel):
    student_result = models.ForeignKey(Result, on_delete= models.DO_NOTHING, related_name='student_result_info')
    student_grade = models.ForeignKey(GradingConfig, on_delete= models.DO_NOTHING, related_name='student_grade_info')



class HolidayManagement(UniversalModel):
    school_holiday = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_holidays')
    slug = AutoSlugField(populate_from=get_school_holiday_slug, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=100, help_text = "Holiday Name")
    holiday_type =  models.CharField(
        max_length=30,
        choices=HolidayType.choices,
        blank=True, null=True
    )
    holiday_start = models.DateField(blank=True, null=True)
    holiday_end = models.DateField(blank=True, null=True)


class FeesCategory(UniversalModel):
    school_fees = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_fees')
    name = models.CharField(max_length=100, help_text = "Fees Name")

    def __str__(self):
        return self.name
    

class FeesInformation(UniversalModel):
    fees_category = models.ForeignKey(FeesCategory, on_delete=models.DO_NOTHING, related_name='school_fees_category')
    fess_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='fess_classes')
    fess_section = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='fess_sections')
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fees_start = models.DateField(blank=True, null=True)
    fees_end = models.DateField(blank=True, null=True)


class FeesCollection(UniversalModel):
    school_fees_collection = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_fees_collection')
    student_fees_collection = models.ForeignKey(Student, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='fees_collection_students')
    fees_collection_category = models.ForeignKey(FeesCategory, on_delete=models.DO_NOTHING, related_name='fees_collection_category')
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_date = models.DateField(auto_now_add=True)