import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from career.models import Company


class Command(BaseCommand):
    help = 'Collects contact information for all companies and saves it to a CSV file.'

    def handle(self, *args, **options):
        companies = Company.objects.all()
        filename = 'company.csv'
        filepath = os.path.join(settings.BASE_DIR, filename)

        with open(filepath, mode='w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'email', 'phone'])
            for company in companies:
                writer.writerow([company.name, company.email, company.phone])

    # def handle(self, *args, **options):
    #     companies = Company.objects.all()
    #     filename = 'company.csv'
    #     filepath = Path(settings.BASE_DIR) / filename
    #
    #     with open(filepath, mode='w') as csv_file:
    #         fieldnames = ['name', 'email', 'phone']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for company in companies:
    #             writer.writerow({'name': company.name, 'email': company.email, 'phone': company.phone})
