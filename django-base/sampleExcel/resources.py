from import_export import resources
from .models import SampleExcelData

class SampleDataResource(resources.ModelResource):
    class Meta:
        model = SampleExcelData