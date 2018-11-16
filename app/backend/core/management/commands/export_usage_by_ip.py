import os

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        # # Positional arguments
        parser.add_argument('destination', type=str)

    def handle(self, *args, **options):
        destination = options['destination']
        file_location = destination if os.path.isdir() else settings.BASE_DIR
        self.stdout.write(
            self.style.SUCCESS(
                f'Success, service usage exported to {file_location}'
            )
        )
