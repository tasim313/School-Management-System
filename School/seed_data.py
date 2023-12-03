#  Create a script to seed your database with fake data. 

from django_seed import Seed
import random

# Your Django models

from core.models import (SchoolClass,
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
    AcademicInformation)

from common.models import(
    SchoolInformationOnBoarding
)
from StudentApp.models import (
    Student,
    StudentImage,
    StudentCurrentStatus,
   
)

seeder = Seed.seeder()

# Register your Django models
seeder.add_entity(SchoolClass, 10)
seeder.add_entity(AcademicInformation, 10)  # Adjust the number as needed
seeder.add_entity(SchoolAdmission, 10)
seeder.add_entity(WebsiteAboutWinningAwards, 10)
seeder.add_entity(WebsiteFunFactContent, 10)
seeder.add_entity( WebsiteAboutFile, 10)
seeder.add_entity(WebsiteAbout, 10)
seeder.add_entity(WebsiteHomeSliderContentFile, 10)
seeder.add_entity(WebsiteHomeSliderContent, 10)
seeder.add_entity(SchoolAddressInformation, 10)
seeder.add_entity(SchoolContactInformation, 10)
seeder.add_entity(WebsiteInformation, 10)
seeder.add_entity(SchoolSection, 10)
seeder.add_entity(SchoolInformationOnBoarding, 10)
seeder.add_entity(StudentImage, 10)
seeder.add_entity(StudentCurrentStatus, 10)

seeder.add_entity(Student, 50)

# Add more models as needed

inserted_pks = seeder.execute()
