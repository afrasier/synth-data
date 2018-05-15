
import pytest
from synth_data.records.factory.django import GivenNameFactory, LocationFactory, StreetNameFactory, StreetSuffixFactory, SecondaryAddressDesignatorFactory


test_factories = [
    (GivenNameFactory),
    (LocationFactory),
    (StreetNameFactory),
    (StreetSuffixFactory),
    (SecondaryAddressDesignatorFactory)
]


@pytest.mark.parametrize('factory', test_factories)
@pytest.mark.django_db()
def test_django_factories(default_records, factory):
    f = factory()

