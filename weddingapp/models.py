from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# needed for Python 2
from weddingapp.utils import code_generator


# RSVP!
@python_2_unicode_compatible
class Invite(models.Model):
    # Code to identify invites by
    code = models.CharField(max_length=6, default=code_generator(4), unique=True)
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # i.e. Shambrook Family
    group_name = models.CharField(max_length=200)
    # number of people in this invite (i.e. husband and wife get one invite)
    group_count = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=12)
    rsvp_completed = models.NullBooleanField(default=False, editable=False)

    def __str__(self):
        return self.group_name


@python_2_unicode_compatible
class Guest(models.Model):
    invite = models.ForeignKey(Invite, on_delete=models.CASCADE)
    # i.e. Billy Shambrook
    guest_name = models.CharField(max_length=200)
    diet = models.CharField(max_length=250, null=True, blank=True)
    transport = models.NullBooleanField(default=False)
    attending = models.NullBooleanField(default=False)

    def __str__(self):
        return self.guest_name
