from django.contrib import admin
from weddingapp.utils import code_generator

from .models import Invite, Guest

admin.site.register(Invite)
admin.site.register(Guest)