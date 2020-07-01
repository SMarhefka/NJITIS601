from django.db import models

class SampleData(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(blank=True, max_length = 254)
	fav_number = models.IntegerField()
	sample_date = models.DateField(null=True, blank=True)

"""
class CharmsDataAll(models.Model):
	charged_center = models.IntegerField()
	effective_date = models.DateField()
	charge_type_desc = models.CharField()
	asset_name = models.CharField()
	environment = models.CharField()
	application_name = models.CharField()
	os = models.CharField()
	location = models.CharField()
	rsm_user_id = models.CharField()
	rsm_user_name = models.CharField()
	volume = models.DecimalField(decimal_places=2)
	rate = models.DecimalField(max_digits=6, decimal_places=2)
	amount = models.DecimalField(decimal_places=2)
	comments = models.TextField()
"""

"""
class CharmsSeverCostData(models.Model):
	environment = models.CharField()
	server_name_app = models.CharField()
	server_namem = models.CharField()
	total_annual_cost = models.DecimalField(decimal_places=2)
"""

