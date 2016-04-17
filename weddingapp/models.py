from __future__ import unicode_literals

import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# needed for Python 2
from weddingapp.utils import code_generator


# from Django's tutorial
# @python_2_unicode_compatible
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# # needed for Python 2
# @python_2_unicode_compatible
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text


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
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    phone_number = models.CharField(validators=[phone_regex], max_length=12)
    rsvp_completed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.group_name


@python_2_unicode_compatible
class Guest(models.Model):
    invite = models.ForeignKey(Invite, on_delete=models.CASCADE)
    # i.e. Billy Shambrook
    guest_name = models.CharField(max_length=200)
    diet = models.CharField(max_length=250)
    transport = models.NullBooleanField(default=False, null=True)
    attending = models.NullBooleanField(null=True)

    def __str__(self):
        return self.guest_name
