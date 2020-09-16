from django.contrib import admin

# Register your models here.
from .models import Players
from .models import Wins

admin.site.register(Players)
admin.site.register(Wins)
