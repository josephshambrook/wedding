from django.contrib import admin
from weddingapp.utils import code_generator

from .models import Invite, Guest

# admin.site.register(Question)
admin.site.register(Invite)
admin.site.register(Guest)

print(code_generator(4))
