from django.contrib import admin
from .models import GeologicalHorizon, TectonicFeature, DensityVelocity

@admin.register(GeologicalHorizon)
class HorizonAdmin(admin.ModelAdmin):
    list_display = ('name', 'depth_min', 'depth_max', 'rock_type', 'gas_present')
    list_filter = ('gas_present',)
    search_fields = ('name',)

@admin.register(TectonicFeature)
class TectonicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DensityVelocity)
class DensityAdmin(admin.ModelAdmin):
    list_display = ('age', 'lithology', 'depth_interval', 'density')