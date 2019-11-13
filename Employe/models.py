from django.db import models

# Create your models here.
class Area(models.Model):
	area_code = models.IntegerField()
	area_name = models.CharField(max_length=50)

	def __str__(self):
		return self.area_name



class Employe(models.Model):
	pass



