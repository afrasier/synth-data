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
            # How many rows?
            'rows': 10,
            # What are the columns?
            'columns': [
                'first_name',
                'last_name',
                'telephone number',
                'ssn',
                'dob',
                'address',
                'city',
                'state',
                'zip'
            ],
            # What factories to use for which column
            'factories': [
                {
                    # Which factory to use
                    "factory": "GivenNameFactory",
                    # Options, which are passed into the factory options parameter
                    "options": {},
                    # Column map - this is used to specify which columns from a record
                    # are mapped to target columns on our generated data
                    "column_map": {
                        "name": "first_name"
                    }
                },
                {
                    "factory": "FamilyNameFactory",
                    "options": {},
                    "column_map": {
                        "name": "last_name"
                    }
                },
                {
                    "factory": "NumberFactory",
                    "options": {
                        "format": "(###) ###-####"
                    },
                    # For non-record factories, you can use an arbitrary string as source column
                    "column_map": {
                        "telno": "telephone number"
                    }
                },
                {
                    "factory": "NumberFactory",
                    "options": {
                        "format": "###-##-####"
                    },
                    # For non-record factories, you can use an arbitrary string as source column
                    "column_map": {
                        "ssn": "ssn"
                    }
                },
                {
                    'factory': 'DateFactory',
                    'options': {
                        'range_start': '1975-01-01T00:00:00Z',
                        'range_end': '2000-01-01T00:00:00Z',
                    },
                    "column_map": {
                        "dob": "dob"
                    }
                },
                {
                    'factory': 'StreetAddressFactory',
                    "column_map": {
                        "name": "address"
                    }
                },
                {
                    'factory': 'LocationFactory',
                    'options': {},
                    "column_map": {
                        "city": "city",
                        "state": "state",
                        "postal_code": "zip"
                    }
                },
            ],
            # All the mutators for this dataset, broken down by column
            'mutators': {
                # Dict of mutator/probability pairs for any/each column
                'first_name': {
                    'mistyped': 0.15
                },
                'last_name': {
                    'misread': 0.5,
                    'misheard': 0.1
                },
                'address': {
                    'mistyped': 0.25
                }
            }
        }

        print(run_job(test_json))
