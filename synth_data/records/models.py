from django.db import models


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
