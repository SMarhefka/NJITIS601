from import_export import resources
from .models import SampleData

class SampleDataResource(resources.ModelResource):
    class Meta:
        model = SampleData