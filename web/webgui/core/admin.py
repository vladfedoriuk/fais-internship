from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(SFibersStackCalibratorPar, SFibersStackDDLookupTable,\
   SFibersStackDDUnpackerPar, SFibersStackDigitizerPar, \
        SFibersStackGeomPar, SFibersStackHitFinderFiberPar, SFibersStackHitFinderPar)
class ConfigurationAdmin(admin.ModelAdmin):
    date_hierarchy = 'valid_from'
    ordering = ('-valid_from', 'version')
    list_display = (
        'valid_from', 'valid_to', 'version', 'release', 'remarks',
    )
    list_filter = ('valid_from', 'valid_to', 'version', 'release')
    search_fields = ('valid_from', 'valid_to', 'version', 'remarks')

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'
    ordering = ('-start_time', 'run_id', 'file_name')
    list_display = ('start_time', 'stop_time', 'run_id', 'file_name', 'remarks')
    list_filter = ('start_time', 'stop_time')
    search_fields = ('file_name', 'run_id', 'remarks', 'start_time', 'stop_time')

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'comment')