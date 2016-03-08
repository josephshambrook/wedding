from __future__ import unicode_literals

import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# needed for Python 2
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# needed for Python 2
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# RSVP!
# needed for Python 2
@python_2_unicode_compatible
class Invite(models.Model):
    code = models.CharField(max_length=6)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # invite_name = models.CharField(max_length=200)
    group_number = models.IntegerField()
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=12)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# needed for Python 2
@python_2_unicode_compatible
class Guest(models.Model):
    invite = models.ForeignKey(Invite, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    diet = models.CharField(max_length=250)
    attending = models.NullBooleanField(null=True)

    def __str__(self):
        return self.name
