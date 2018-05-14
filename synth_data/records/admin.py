from django.contrib import admin

from synth_data.records.models import GivenName, FamilyName, Location, StreetName, StreetSuffix, SecondaryAddressDesignator

# Register all of our models here with the admin site
models = [
    GivenName,
    FamilyName,
    Location,
    StreetName,
    StreetSuffix,
    SecondaryAddressDesignator
]

for model in models:
    admin.site.register(model)
