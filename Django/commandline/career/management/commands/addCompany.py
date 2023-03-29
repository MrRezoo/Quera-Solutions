import re

from django.core.management.base import BaseCommand

from career.models import Company


class Command(BaseCommand):
    help = 'Creates a new company'

    def handle(self, *args, **options):
        name = self.name_validator()
        email = self.email_validator()
        phone = self.phone_validator()
        description = input('Description: ') or None

        Company.objects.create(
            name=name,
            email=email,
            phone=phone,
            description=description,
        )

    def name_validator(self):
        while True:
            name = input('Name: ')
            if not name:
                error_msg = "Error: This field cannot be blank."
            elif len(name) > 50:
                error_msg = f'Error: Ensure this value has at most 50 characters (it has {len(name)}).'
            elif Company.objects.filter(name=name).exists():
                error_msg = 'Error: That name is already taken.'
            else:
                return name
            self.stderr.write(error_msg)

    def email_validator(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        while True:
            email = input('Email: ')
            if not email:
                error_msg = "Error: This field cannot be blank."
            elif not re.match(pattern, email):
                error_msg = 'Error: Enter a valid email address.'
            else:
                return email
            self.stderr.write(error_msg)

    def phone_validator(self):
        pattern = r'^(0|\+98|0098)9[0-9]{9}$'
        while True:
            phone = input('Phone: ')
            if not phone:
                error_msg = "Error: This field cannot be blank."
            elif not re.match(pattern, phone):
                error_msg = 'Error: Phone number format is not valid.'
            else:
                return phone
            self.stderr.write(error_msg)