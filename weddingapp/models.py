from __future__ import unicode_literals

import random
import string

from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# needed for Python 2
# from weddingapp.utils import code_generator


def code_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# RSVP!
@python_2_unicode_compatible
class Invite(models.Model):
    # Code to identify invites by
    code = models.CharField(max_length=6, default=code_generator(4), unique=True)
    # i.e. Shambrook Family
    group_name = models.CharField(max_length=200)
    # number of people in this invite (i.e. husband and wife get one invite)
    group_count = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=12)
    song_requests = models.CharField(max_length=250, null=True, blank=True)
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


GIFT_CATEGORIES = (
    ('kitchen', 'Kitchen'),
    ('electric', 'Electric Items'),
    ('crockery', 'Crockery'),
    ('glass', 'Glasses'),
    ('cutlery', 'Cutlery'),
    ('knives', 'Knives'),
    ('pots_pans', 'Pots and Pans'),
    ('linens', 'Linens'),
    ('house', 'Houseware'),
    ('other', 'Other')
)


@python_2_unicode_compatible
class Gift(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.IntegerField(blank=True, null=True)
    actual = models.CharField(
        max_length=200,
        choices=(('exact', 'Exact'), ('similar', 'Similar')),
        default='exact',
        blank=True
    )
    category = models.CharField(
        max_length=200,
        choices=GIFT_CATEGORIES,
        default='kitchen'
    )
    url = models.URLField(blank=True, max_length=200)

    def __str__(self):
        return self.item


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    google_link = models.URLField(blank=True, max_length=200)
    website_link = models.URLField(blank=True, max_length=200)
