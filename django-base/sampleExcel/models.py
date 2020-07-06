from django.db import models
from django.forms import ModelForm

# Create your models here.
class SampleExcelData(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(null=True, blank=True, max_length = 254)
	fav_number = models.IntegerField()
	date = models.DateField(null=True, blank=True)

class SampleExcelForm(ModelForm):
	class Meta:
		model = SampleExcelData
		fields = ['first_name', 'last_name', 'email', 'fav_number', 'date']