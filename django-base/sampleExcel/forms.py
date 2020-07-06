from django import forms
from django.forms import ModelForm
from .models import SampleExcelData

class SampleFormData(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()


"""
class TestForms(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20)
	last_name = forms.CharField(label='Last Name', max_length=20)
	email = forms.EmailField(blank=True, max_length = 254)
	fav_number = forms.IntegerField()
	sample_date = forms.DateField(null=True, blank=True)
"""