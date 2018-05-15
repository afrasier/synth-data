from django.db import models
from django.contrib.postgres.fields import JSONField


class Job(models.Model):
    '''
    Represents a synthesization job

    The job is represented by a json object detailing the format and labeling of the data. The job will generate a "pure" dataset, and then a
    mutated dataset, using specified mutators.

    example
    {
        'rows': 1000,
        'columns': {
            'first_name': {
                'factory': 'GivenNameFactory',
                'options': {
                    'sex': 'male'
                },
                'mutators': {
                    'transposition': 0.1
                }
            },
            'tel_no': {
                'factory': 'NumberFactory',
                'options': {
                    'format': '(###) ###-####'
                },
                'mutators': {
                    'misheard': 0.01
                }
            }
        }
    }
    '''

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text="The user who owns this job")

    job = JSONField(help_text="JSON describing the job")
    running = models.BooleanField(default=False, help_text="Flag indicating if this job is currently running")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(null=True)

    @property
    def filename(self) -> str:
        return f"{self.id}-{self.user.username}"
