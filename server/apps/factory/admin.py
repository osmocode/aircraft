from django.contrib import admin
from .models import AircraftModelFactory, AircraftPartFactory

# Register your models here.
@admin.register(AircraftModelFactory)
class AircraftModelFactoryAdmin(admin.ModelAdmin):
  list_display = ['model_type', 'made_by', 'made_at']

@admin.register(AircraftPartFactory)
class AircraftPartFactoryAdmin(admin.ModelAdmin):
  list_display = ['part_type', 'part_of', 'made_by', 'made_at']