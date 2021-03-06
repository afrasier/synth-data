import pandas
import logging

from pydoc import locate

'''
This file contains factories which generate their data (rather than randomizing known records)
'''


class GeneratorFactory():
    '''
    This factory uses some generator to create and fill data into a dataframe
    '''

    MAX_BATCH_SIZE = 100000
    GENERATOR = ""

    def __init__(self, options: dict):
        '''
        Initialize the factory - options are passed to the generator as kwargs
        '''
        self.logger = logging.getLogger(__name__)
        self.options = options

        self.generator = locate(self.GENERATOR)(**options)

    def create_rows(self, count: int, columns: list):
        dataframe = pandas.DataFrame(columns=columns)

        while dataframe.empty or dataframe.shape[0] < count:
            # Create a list of lists of generator data for each column
            dataframe_data = {col: [next(self.generator) for _ in range(0, min(count - dataframe.shape[0], self.MAX_BATCH_SIZE))] for col in columns}

            dataframe = pandas.concat([dataframe, pandas.DataFrame(dataframe_data)], ignore_index=True)

        return dataframe.truncate(after=count)


class NumberFactory(GeneratorFactory):

    GENERATOR = "synth_data.records.generators.number_generator"


class NumberRangeFactory(GeneratorFactory):

    GENERATOR = "synth_data.records.generators.range_generator"


class DateFactory(GeneratorFactory):

    GENERATOR = "synth_data.records.generators.date_generator"

    def create_rows(self, *args, **kwargs):
        df = super(DateFactory, self).create_rows(*args, **kwargs)
        # Conver the data to pandas datetimes
        df[kwargs.get('columns')] = df[kwargs.get('columns')].apply(pandas.to_datetime)
        return df
