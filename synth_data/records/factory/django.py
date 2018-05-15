import pandas
import logging

from pydoc import locate
from django_pandas.io import read_frame
from django.db.models import Q

'''
This file contains factories which, once initialized, can create arbitrarily sized
dataframe columns filled with randomized data
'''


class DjangoModelFactory():

    '''
    The factory datatype denotes the type of data generated by this factory,
    which is used to ensure an associated mutator can effectively mutate data
    generated by this factory
    '''
    FACTORY_DATATYPE = str
    DJANGO_MODEL = None
    DEFAULT_COLUMNS = []

    def __init__(self, options: dict = None):
        '''
        Creates a given name factory
        '''
        self.options = options
        self.django_class = locate(self.DJANGO_MODEL)
        self.django_instance_count = self.django_class.objects.count()

        self.logger = logging.getLogger(__name__)

        # Turn our options dict into a Q object
        if self.options:
            self.options = Q(**self.options)
        else:
            self.options = Q()

        if self.django_instance_count == 0:  # pragma: no cover
            self.logger.warning(f"There are no avaialble records for {self.DJANGO_MODEL}")

    def create_rows(self, count: int, columns: str = None) -> pandas.DataFrame:
        '''
        Create a dataframe with the specified number of rows, and the requested columns,
        if no columns are specified, default columns will be returned
        '''
        if not columns:
            columns = self.DEFAULT_COLUMNS

        dataframe = pandas.DataFrame(columns=columns)

        while dataframe.empty or dataframe.shape[0] < count:
            records = self.django_class.objects.all().filter(self.options).order_by('?').values(*columns)[:min(count - dataframe.shape[0], self.django_instance_count)]
            if records.count() == 0:  # pragma: no cover
                self.logger.warning(f"Could not find any records for {self.DJANGO_MODEL} with options {self.options}")
                return dataframe
            df = read_frame(records)
            dataframe = pandas.concat([dataframe, df], ignore_index=True)

        return dataframe.truncate(after=count)


class GivenNameFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.GivenName"
    DEFAULT_COLUMNS = ["name"]


class FamilyNameFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.FamilyName"
    DEFAULT_COLUMNS = ["name"]


class LocationFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.Location"
    DEFAULT_COLUMNS = ["city", "state"]


class StreetSuffixFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.StreetSuffix"
    DEFAULT_COLUMNS = ["name", "abbreviation"]


class StreetNameFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.StreetName"
    DEFAULT_COLUMNS = ["name"]


class SecondaryAddressDesignatorFactory(DjangoModelFactory):

    DJANGO_MODEL = "synth_data.records.models.SecondaryAddressDesignator"
    DEFAULT_COLUMNS = ["name", "abbreviation"]
