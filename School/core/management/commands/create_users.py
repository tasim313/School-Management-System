import factory
from factory.django import DjangoModelFactory

from django.core.management.base import BaseCommand

from school_auth.models import User
from faker import Faker

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"test_user_{n}")
    role = "student"
    is_active = True
    firstName = fake.first_name()
    lastName = fake.last_name()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating user instances using Factory")
        users = UserFactory.create_batch(20)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(users)} user instances"))
