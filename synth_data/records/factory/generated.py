import pytest

from model_mommy import mommy

from synth_data.records.factory.django import GivenNameFactory, LocationFactory, StreetNameFactory, StreetSuffixFactory, SecondaryAddressDesignatorFactory

test_factories = [
    (GivenNameFactory),
    (LocationFactory),
    (StreetNameFactory),
    (StreetSuffixFactory),
    (SecondaryAddressDesignatorFactory),
]


@pytest.mark.parametrize("factory", test_factories)
@pytest.mark.django_db()
def test_django_factories(factory):
    f = factory()
    mommy.make(f.django_class, _quantity=10)

    assert f.create_rows(count=10).shape[0] == 10
    assert f.create_rows(count=1000).shape[0] == 1000
