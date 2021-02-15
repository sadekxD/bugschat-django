from django.contrib import admin
from .models import Message, Contact

admin.site.register(Contact)
admin.site.register(Message)
