from django.contrib import admin
from weddingapp.utils import code_generator

from .models import Invite

# admin.site.register(Question)
admin.site.register(Invite)

print(code_generator(4))
