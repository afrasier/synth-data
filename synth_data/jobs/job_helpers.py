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

    factory_classes = {
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
    factories = job_json.get('factories')

    logger.info(f"Sythesizing {num_rows} for columns {columns}")

    dataframe = pandas.DataFrame(columns=columns)

    for f in factories:
        factory = f.get('factory')
        options = f.get('options')

        factory = locate(factory_classes[factory])(options=options)

        column_map = f.get('column_map')

        factory_output = factory.create_rows(count=num_rows, columns=list(column_map.keys()))

        for df_col, target_col in column_map.items():
            dataframe[target_col] = factory_output[df_col]

    pure_file = tempfile.NamedTemporaryFile(delete=False)
    dataframe.to_csv(pure_file.name, index_label="index")

    logger.info(f"Sythesis complete, elapsed time: {format_seconds((datetime.datetime.now() - start).total_seconds())}")

    return {
        "pure_file": pure_file.name
    }
