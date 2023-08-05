# jobs/management/commands/add_sample_jobs.py

from django.core.management.base import BaseCommand
from jobs.models import Job

class Command(BaseCommand):
    help = 'Adds sample job data to the database'

    def handle(self, *args, **kwargs):
        # Sample job data
        sample_jobs = [
            {
                'title': 'Software Engineer',
                'location': 'Bangalore',
                'description': 'Job description for Software Engineer.',
            },
            {
                'title': 'Product Manager',
                'location': 'Mumbai',
                'description': 'Job description for Product Manager.',
            },
            {
                'title': 'Data Scientist',
                'location': 'Delhi',
                'description': 'Job description for Data Scientist.',
            },
        ]

        for job_data in sample_jobs:
            job = Job.objects.create(**job_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added job: {job.title}'))
