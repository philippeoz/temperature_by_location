import os
import itertools
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Avg, Count
from django.utils import timezone

from backend.core.models import IPRequestLog


class Command(BaseCommand):
    """Command to export usage count by days"""

    def add_arguments(self, parser):
        parser.add_argument(
            '--path', dest='path', type=str, help="Optional dir to save file"
        )

    def handle(self, *args, **options):
        destination = options['path']
        file_location = destination if destination and os.path.isdir(
            destination
        ) else settings.BASE_DIR

        usage_count_queryset = IPRequestLog.objects.extra(
            {'created_day':"to_char(date(created_at), 'YYYY-MM-DD')"}
        ).values('created_day', 'ip').annotate(count=Count('ip'))

        data = {}
        for record in usage_count_queryset:
            if record['created_day'] not in data.keys():
                data[record['created_day']] = []
            data[record['created_day']].append(
                {'ip': record['ip'], 'usage_count': record['count']}
            )

        file_name = 'usage_by_ip_{}.json'.format(
            timezone.now().strftime("%Y%m%d%H%M%S")
        )

        file_location = os.path.join(file_location, file_name)

        with open(file_location, 'w') as dump_file:
            dump_file.write(json.dumps(data))
            dump_file.close()

        self.stdout.write(
            self.style.SUCCESS(
                f'Success, service usage exported to {file_location}'
            )
        )
