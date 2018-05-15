import logging

from django.core.management.base import BaseCommand

from synth_data.jobs.job_helpers import run_job


class Command(BaseCommand):
    help = 'Loads a CSV into a supported model'
    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        test_json = {
            'rows': 100000,
            'columns': {
                'first_name': {
                    'factory': 'GivenNameFactory',
                    'options': {
                        'sex': 'M'
                    },
                    'use_column': 'name',
                    'mutators': {
                        'transposition': 0.1
                    }
                },
                'last_name': {
                    'factory': 'FamilyNameFactory',
                    'use_column': 'name',
                    'mutators': {
                        'transposition': 0.1
                    }
                },
                'ssn': {
                    'factory': 'NumberFactory',
                    'options': {
                        'format': '###-##-####'
                    },
                },
                'dob': {
                    'factory': 'DateFactory',
                    'options': {
                        'range_start': '1975-01-01T00:00:00Z',
                        'range_end': '2000-01-01T00:00:00Z',
                    },
                },
                'address': {
                    'factory': 'StreetAddressFactory',
                },
                'city': {
                    'factory': 'LocationFactory',
                    'use_column': 'city'
                },
                'state': {
                    'factory': 'LocationFactory',
                    'use_column': 'state'
                },
                'zip': {
                    'factory': 'LocationFactory',
                    'use_column': 'postal_code'
                }
            }
        }

        print(run_job(test_json))
