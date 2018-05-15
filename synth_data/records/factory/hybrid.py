import random
import pandas

from synth_data.records.factory.generated import NumberRangeFactory, NumberFactory
from synth_data.records.factory.django import StreetNameFactory, StreetSuffixFactory, SecondaryAddressDesignatorFactory

'''
Hybrid factories which combine many record based and generator based factories
'''


class StreetAddressFactory():

    def __init__(self, options: dict):
        self.options = options

        self.random = random.SystemRandom()
        self.street_name_factory = StreetNameFactory()
        self.street_suffix_factory = StreetSuffixFactory()
        self.sec_designator_factory = SecondaryAddressDesignatorFactory()
        self.street_number_factory = NumberRangeFactory(options={'start': 100, 'end': 9999})
        self.sec_designator_number_factory = NumberFactory(options={'format': '##'})

    def create_rows(self, count: int, columns: list):
        def set_at_random(chance: float, original_value, target_value):
            if self.random.random() <= chance:
                return target_value
            else:
                return original_value

        street_names = self.street_name_factory.create_rows(count=count, columns=['name'])
        suffixes = self.street_suffix_factory.create_rows(count=count, columns=['abbreviation'])
        designators = self.sec_designator_factory.create_rows(count=count, columns=['abbreviation'])

        street_numbers = self.street_number_factory.create_rows(count=count, columns=['street_no'])
        sec_designator_nums = self.sec_designator_number_factory.create_rows(count=count, columns=['no'])

        designators['abbreviation'] = designators['abbreviation'].map(lambda x: set_at_random(0.25, x, "# "))
        designators['abbreviation'] = designators['abbreviation'].str.cat(sec_designator_nums['no'].astype(str), sep=' ')
        designators['abbreviation'] = designators['abbreviation'].map(lambda x: set_at_random(0.9, x, ""))

        street_names['name'] = street_numbers['street_no'].str.cat([street_names['name'], suffixes['abbreviation'], designators['abbreviation']], sep=' ')

        return street_names
