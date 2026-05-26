from django.contrib import admin
from .models import Seismic3DParams, FoldMapImage

@admin.register(Seismic3DParams)
class ParamsAdmin(admin.ModelAdmin):
    list_display = ('param_name', 'value', 'unit')
    search_fields = ('param_name',)

@admin.register(FoldMapImage)
class FoldMapAdmin(admin.ModelAdmin):
    list_display = ('title',)
