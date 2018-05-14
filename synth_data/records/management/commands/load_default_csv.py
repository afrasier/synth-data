import logging
import os
import datetime

from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings

from synth_data.common.common_helpers import format_seconds


class Command(BaseCommand):
    help = 'Loads all of the default CSVs into the database, from the raw_data folder'
    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.modes = {
            'given_name': '2010_SSA_baby_names.csv',
            'family_name': '2010_Census_Surnames.csv',
            'location': '2012_Zipcode_City_State.csv',
            'street_suffix': '2017_USPS_Street_Suffixes.csv',
            'street_name': '1993_Census_Common_Street_Names.csv',
            'secondary_designator': '2017_USPS_Secondary_Designators.csv'
        }

    def handle(self, *args, **options):
        start = datetime.datetime.now()
        self.logger.info("Now loading all default CSVs...")

        for mode, file in self.modes.items():
            call_command("load_csv", os.path.join(settings.BASE_DIR, "synth_data", "raw_data", file), mode)

        self.logger.info(f"Loaded all CSVs, elapsed time: {format_seconds((datetime.datetime.now() - start).total_seconds())}")
