from django.db import models

'''
Records represent non-mutated data that can be used to generate synthesized datasets
'''


class GivenName(models.Model):
    '''
    Represents a given (first) name
    '''

    name = models.CharField(max_length=120, help_text="The given name")
    sex = models.CharField(max_length=1, help_text="A flag indicating the general sex of the name")

    def __str__(self):
        return self.name


class FamilyName(models.Model):
    '''
    Reperesents a given family name (surname)
    '''

    name = models.CharField(max_length=120, help_text="The family name")

    def __str__(self):
        return self.name


class Location(models.Model):
    '''
    Represents a geographic location, generally by city and province/state
    '''

    city = models.CharField(max_length=120, help_text="The city name")
    state = models.CharField(max_length=120, help_text="The state (or province) name")

    postal_code = models.CharField(max_length=5, help_text="The 5-digit postal code")
    postal_code_type = models.CharField(max_length=120, help_text="The postal code type")

    latitude = models.FloatField(null=True, help_text="The latitude of the location")
    longitude = models.FloatField(null=True, help_text="The longitude of the location")

    def __str__(self):
        return f"{self.city}, {self.state}"


class StreetSuffix(models.Model):
    '''
    Represents a street suffix (e.g., Street, Place, Alley)
    '''

    name = models.CharField(max_length=120, help_text="The colloquial name for the suffix")
    abbreviation = models.CharField(max_length=12, help_text="The standard abbreviation for this suffix")

    def __str__(self):
        return self.name


class StreetName(models.Model):
    '''
    Represents a street name
    '''

    name = models.CharField(max_length=120, help_text="The street name")

    def __str__(self):
        return self.name


class SecondaryAddressDesignator(models.Model):
    '''
    Represents a secondary address designator (e.g. Apartment, Suite)
    '''

    name = models.CharField(max_length=120, help_text="The full name of the designator")
    abbreviation = models.CharField(max_length=12, help_text="The designator's abbreviation")

    def __str__(self):
        return self.name
