import logging
import pandas
import datetime

from pydoc import locate
from django.core.management.base import BaseCommand

from synth_data.common.common_helpers import format_seconds


class Command(BaseCommand):
    help = 'Loads a CSV into a supported model'
    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.modes = {
            'given_name': mode_given_name,
            'family_name': mode_family_name,
        }

    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str, help="The CSV file to load")
        parser.add_argument('type', nargs=1, type=str, choices=self.modes.keys(), help="The type of data in the CSV")

    def handle(self, *args, **options):
        start = datetime.datetime.now()
        model, column_map = self.modes[options['type'][0]]()

        self.logger.info(f"Loading CSV...\n\tFile: {options['file'][0]}\n\tModel: {model}")

        # Load the file into a pandas dataframe
        df = pandas.read_csv(options['file'][0])

        # Filter to only columns we are expecting
        df = df.filter(items=column_map.keys())

        # Rename the columns
        df = df.rename(index=str, columns=column_map)

        self.logger.info(f"CSV loaded into dataframe: {df.shape[0]} rows, {df.shape[1]} columns")
        df_columns = '\n\t'.join(df.keys())
        self.logger.info(f"Columns:\n\t{df_columns}")

        # Create instances
        instances = []
        instance_class = locate(model)

        self.logger.info(f"There are currently {instance_class.objects.count()} instances of {model} in the database.")

        for index, row in df.iterrows():
            instances.append(instance_class(**row.to_dict()))

        self.logger.info(f"Created {len(instances)} instances of {model}, inserting into database...")
        instance_class.objects.bulk_create(instances)

        self.logger.info(f"Insertion complete. There are now {instance_class.objects.count()} instances of {model} in the database.")
        self.logger.info(f"Elapsed time: {format_seconds((datetime.datetime.now() - start).total_seconds())}")


def mode_given_name():
    model = "synth_data.records.models.GivenName"

    # A map from CSV column headers model fields
    column_map = {
        "Name": "name",
        "sex": "sex"
    }

    return (model, column_map)


def mode_family_name():
    model = "synth_data.records.models.FamilyName"

    # A map from CSV column headers model fields
    column_map = {
        "Name": "name",
    }

    return (model, column_map)
