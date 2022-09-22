from django.contrib import admin
from .models import Ship
from .models import Battlesite

# Register your models here.
admin.site.register(Ship)
admin.site.register(Battlesite)