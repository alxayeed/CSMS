from django.db import models

# Create your models here.
class Area(models.Model):
	area_code = models.IntegerField()
	area_name = models.CharField(max_length=50)

	def __str__(self):
		return self.area_name



class Employe(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	contact_no = models.PositiveSmallIntegerField()
	work_area = models.ForeignKey(Area,on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	date_joined = models.DateField(auto_now_add=True) 
	

	def __str__(self):
		return self.name  



