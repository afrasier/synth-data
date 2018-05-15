
import pytest
from synth_data.records.factory.django import GivenNameFactory, LocationFactory, StreetNameFactory, StreetSuffixFactory, SecondaryAddressDesignatorFactory


test_factories = [
    (GivenNameFactory, None),
    (GivenNameFactory, {'sex': 'M'}),
    (LocationFactory, None),
    (StreetNameFactory, None),
    (StreetSuffixFactory, None),
    (SecondaryAddressDesignatorFactory, None),
]


@pytest.mark.parametrize('factory, options', test_factories)
@pytest.mark.django_db()
def test_django_factories(default_records, factory, options):
    f = factory(options=options)

    assert f.create_rows(count=5).shape[0] == 5
    assert f.create_rows(count=100).shape[0] == 100
