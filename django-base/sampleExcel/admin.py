from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SampleExcelData

# Register your models here.
@admin.register(SampleExcelData)
class SampleExcelDataAdmin(ImportExportModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'fav_number', 'date')
