from django.contrib import admin

from .models import Invite, Guest

admin.site.register(Invite)
admin.site.register(Guest)