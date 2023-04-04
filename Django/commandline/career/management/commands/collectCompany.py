import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from career.models import Company


class Command(BaseCommand):
    help = 'Collects information of all companies and writes to a csv file.'

    def handle(self, *args, **options):
        companies = Company.objects.all()
        filename = 'company.csv'
        filepath = os.path.join(settings.BASE_DIR, filename)

        with open(filepath, mode='w') as csvfile:
            writer = csv.writer(csvfile)
            for company in companies:
                writer.writerow([company.name, company.email, company.phone])
