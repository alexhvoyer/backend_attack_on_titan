from django.contrib import admin

# Register your models here.
from .models import Character
from .models import Titan

admin.site.register(Character)
admin.site.register(Titan)
