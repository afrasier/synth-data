import pandas
import logging
import datetime
import tempfile

from pydoc import locate

from synth_data.common.common_helpers import format_seconds


def run_job(job_json: dict) -> dict:
    '''
    Runs the job as detailed by the json specified, returning a dict of filenames
    for the output CSV
    '''

    start = datetime.datetime.now()
    logger = logging.getLogger(__name__)

    factories = {
        "GivenNameFactory": "synth_data.records.factory.django.GivenNameFactory",
        "FamilyNameFactory": "synth_data.records.factory.django.FamilyNameFactory",
        "LocationFactory": "synth_data.records.factory.django.LocationFactory",
        "StreetNameFactory": "synth_data.records.factory.django.StreetNameFactory",
        "StreetSuffixFactory": "synth_data.records.factory.django.StreetSuffixFactory",
        "SecondaryAddressDesignatorFactory": "synth_data.records.factory.django.SecondaryAddressDesignatorFactory",

        "NumberFactory": "synth_data.records.factory.generated.NumberFactory",
        "DateFactory": "synth_data.records.factory.generated.DateFactory",

        "StreetAddressFactory": "synth_data.records.factory.hybrid.StreetAddressFactory",
    }

    num_rows = job_json.get('rows')
    columns = job_json.get('columns')

    logger.info(f"Sythesizing {num_rows} for columns {columns.keys()}")

    dataframe = pandas.DataFrame(columns=columns.keys())

    for column, specification in columns.items():
        # TODO: Gather shared factories (like Location)
        factory = specification.get('factory', None)

        if not factory:
            raise Exception(f"{column} has no specified factory.")

        options = specification.get('options', None)

        factory = locate(factories[factory])(options=options)

        use_column = specification.get('use_column', column)

        df_column = factory.create_rows(count=num_rows, columns=[use_column])

        dataframe[column] = df_column

    pure_file = tempfile.NamedTemporaryFile(delete=False)
    dataframe.to_csv(pure_file.name)

    logger.info(f"Sythesis complete, elapsed time: {format_seconds((datetime.datetime.now() - start).total_seconds())}")

    return {
        "pure_file": pure_file.name
    }
