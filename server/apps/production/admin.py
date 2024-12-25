from django.contrib import admin
from .models import AircraftModel, AircraftPart

# Register your models here.

@admin.register(AircraftModel)
class AircraftModelAdmin(admin.ModelAdmin):
  list_display = ['name', 'desc']

@admin.register(AircraftPart)
class AircraftPartAdmin(admin.ModelAdmin):
  list_display = ['name', 'desc']