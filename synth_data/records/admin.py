from django.contrib import admin

from synth_data.records.models import GivenName, FamilyName

# Register all of our models here with the admin site
models = [
    GivenName,
    FamilyName
]

for model in models:
    admin.site.register(model)
