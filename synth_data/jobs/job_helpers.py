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

    logger.info(f"Processing job requirements...")

    '''
    Parse our job to combine factories which should only be instantiated once (Record/Django factories)
    {
        "columns": [
            ....
        ],
        "factories": [
            {
                "factory": "synth_databAADLFALSDFLASDF",
                "column_map": {
                    "use_column": "target_column"
                },
                "options": {
                    "combinedoptions"
                }
            }
        ]
    }
    '''

    gathered_job = {
        "columns": [],
        "factories": []
    }

    for column, specification in columns.items():
        gathered_job["columns"].append(column)

        factory = specification.get('factory', None)

        if not factory:
            raise Exception(f"{column} has no specified factory.")

        factory_object = {
            "factory": factory,
            "column_map": {},
            "options": {}
        }

        if 'django' in factory:
            existing_factory = [x for x in gathered_job['factories'] if x.factory == factory]
            if len(existing_factory) == 1:
                factory_object = existing_factory[0]
            elif len(existing_factory) > 1:
                logger.warning(f"Multiple factories for {factory} while running job.")

        # Map columns
        factory_object["column_map"][specification.get("use_column", column)] = column
        # Combine options
        factory_object["options"] = {**factory_object["options"], **specification.get('options', {})}

        gathered_job["factories"].append(factory_object)

    logger.info(f"Sythesizing {num_rows} for columns {gathered_job['columns']}")

    dataframe = pandas.DataFrame(columns=gathered_job['columns'])

    for f in gathered_job['factories']:
        factory = f.get('factory')
        options = f.get('options')

        factory = locate(factories[factory])(options=options)

        column_map = f.get('column_map')

        factory_output = factory.create_rows(count=num_rows, columns=list(column_map.keys()))

        for df_col, target_col in column_map.items():
            dataframe[target_col] = factory_output[df_col]

    pure_file = tempfile.NamedTemporaryFile(delete=False)
    dataframe.to_csv(pure_file.name)

    logger.info(f"Sythesis complete, elapsed time: {format_seconds((datetime.datetime.now() - start).total_seconds())}")

    return {
        "pure_file": pure_file.name
    }
