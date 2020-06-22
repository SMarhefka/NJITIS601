from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SampleData

# Register your models here.
@admin.register(SampleData)
class SampleDataAdmin(ImportExportModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'fav_number')
