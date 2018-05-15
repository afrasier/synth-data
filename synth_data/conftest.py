import pytest

from model_mommy import mommy
from itertools import cycle


@pytest.fixture()
@pytest.mark.django_db()
def default_records():
    male_names = ["Han", "Lando", "Mace", "Shreev", "Luke"]
    female_names = ["Leia", "Beru", "Padme", "Rose", "Rey"]
    family_names = ["Skywalker", "Windu", "Palpatine", "Amidala", "Kenobi", "Smith"]

    mommy.make('records.GivenName', name=cycle(male_names), sex='M', _quantity=len(male_names))
    mommy.make('records.GivenName', name=cycle(female_names), sex='F', _quantity=len(female_names))

    mommy.make('records.FamilyName', name=cycle(family_names), _quantity=len(family_names))

    cities = ["Washington", "Los Angeles", "Chicago"]
    state = ["CA", "AL", "NY", "FL"]
    postal_codes = ["90210", "20148", "11345", "56323"]

    mommy.make('records.Location', city=cycle(cities), state=cycle(state), postal_code=cycle(postal_codes), _quantity=10)

    street_names = ["2nd", "Branch", "Peachtree", "Green", "Main"]

    mommy.make('records.StreetName', name=cycle(street_names), _quantity=len(street_names))

    suffixes = ["Place", "Crescent", "Circle", "Way"]

    mommy.make('records.StreetSuffix', name=cycle(suffixes), _quantity=len(suffixes))

    sec_designators = ["Apt", "Ste", "Fl", "Bsmnt"]

    mommy.make('records.SecondaryAddressDesignator', name=cycle(sec_designators), _quantity=len(sec_designators))
