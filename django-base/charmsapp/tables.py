import django_tables2 as tables
from .models import SampleData


from django.db.models.functions import Length

class SampleDataTable(tables.Table):
    class Meta:
        model = SampleData
        attrs = {'class': 'table table-sm', 'id':'example'}
        fields = ("id", "first_name", "last_name", "email", "fav_number", "sample_date", "action")