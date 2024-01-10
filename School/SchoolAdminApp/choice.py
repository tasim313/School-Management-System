from django.db import models


class Gender(models.TextChoices):
    FEMALE = "female", "Female"
    MALE = "male", "Male"
    OTHERS = "others", "Others"



class JobType(models.TextChoices):
    FullTime = 'full_time', 'Full Time'
    PartTime = 'part_time', 'Part Time'
    Internship = 'internship', 'Internship'
    Temporary = 'temporary', 'Temporary'
    Remote = 'remote', 'Remote'
    Other = 'other', "Other"



class JobStatus(models.TextChoices):
    Open = 'open', 'Open'
    Closed = 'closed', 'Closed'
    Cancelled = 'cancelled', 'Cancelled'


class BookType(models.TextChoices):
    Book = 'book', 'Book'
    DVD = 'dvd', 'DVD'
    CD = 'cd', 'CD'
    Newspaper = 'newspaper', 'Newspaper'


class BookStatus(models.TextChoices):
    InStock = 'in_stock', 'In Stock'
    OutOfStock = 'out_of_stock', 'Out Of Stock'


class HostelRoomType(models.TextChoices):
    Normal = 'normal', 'Normal'
    AC = 'ac', 'AC'
    Suite = 'suite', 'Suite'

class HostelAvailability(models.TextChoices):
    Available = 'available', 'Available'
    NotAvailable = 'not_available', 'Not Available'