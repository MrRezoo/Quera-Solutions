import re

from django.core.management.base import BaseCommand, CommandError

from career.models import Company


class Command(BaseCommand):
    help = 'Updates the fields of a company'

    def add_arguments(self, parser):
        parser.add_argument('company_name', type=str, help='Name of the company')
        parser.add_argument('--name', type=str, help='New name for the company')
        parser.add_argument('--email', type=str, help='New email for the company')
        parser.add_argument('--phone', type=str, help='New phone number for the company')
        parser.add_argument('--description', type=str, help='New description for the company')

    def handle(self, *args, **options):
        try:
            # Get the company with the given name
            company = Company.objects.get(name=options['company_name'])
        except Company.DoesNotExist:
            raise CommandError('Company matching query does not exist.')

        for key in ['name', 'email', 'phone', 'description']:
            if not company._meta.get_field(key).null and options[key] == '':
                raise CommandError(f'{key.capitalize()} cannot be blank.')

            elif company._meta.get_field(key).null and options[key] == '':
                options[key] = None

        # Update the fields of the company
        if options['description'] is not None:
            company.description = options['description']

        if options['phone'] is not None:
            if self.phone_validator(options['phone']):
                company.phone = options['phone']
            else:
                raise CommandError('Error: Phone number format is not valid.')

        if options['email']:
            if validate_email(options['email']):
                company.email = options['email']
            else:
                raise CommandError('Error: Enter a valid email address.')

        if options['name']:
            if len(options['name']) > 50:
                raise CommandError(
                    f'Error: Ensure this value has at most 50 characters (it has {len(options["name"])}).')
            elif Company.objects.filter(name=options['name']).exists():
                raise CommandError('Error: That name is already taken.')
            else:
                company.name = options['name']

        # Save the changes to the database
        try:
            company.full_clean()
            company.save()
        except Exception as e:
            field_name = str(e).split('.')[2].split(':')[0]
            raise CommandError(f'{field_name.capitalize()} cannot be blank.')

    def phone_validator(self, phone):
        pattern = r'^(0|\+98|0098)9[0-9]{9}$'

        if not re.match(pattern, phone):
            return False
        return True


def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
