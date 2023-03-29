from django.core.management.base import BaseCommand, CommandError
from career.models import Company


class Command(BaseCommand):
    help = 'Removes the given company/companies from the database'

    def add_arguments(self, parser):
        parser.add_argument('company_names', nargs='*', type=str, help='Name of the company/companies to be removed')
        parser.add_argument('--all', action='store_true', help='Removes all companies')

    def handle(self, *args, **options):
        if options['all']:
            Company.objects.all().delete()
        else:
            for name in options['company_names']:
                try:
                    company = Company.objects.get(name=name)
                    company.delete()
                except Company.DoesNotExist:
                    error_msg = f"{name} matching query does not exist."
                    self.stderr.write(error_msg)

