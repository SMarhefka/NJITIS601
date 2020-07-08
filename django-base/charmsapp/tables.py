import django_tables2 as tables
from .models import SampleData

class SampleDataTable(tables.Table):
    class Meta:
        model = SampleData
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "first_name", "last_name", "email", "fav_number")
        orderable = True