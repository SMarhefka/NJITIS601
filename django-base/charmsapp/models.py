from django.db import models

# Create your models here.
# class AllCharmsData(models.Model):
#	charged_center = models.IntegerField()
#	effective_date = models.DateFimeField()

class SampleData(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(blank=True, max_length = 254)
	fav_number = models.IntegerField()
