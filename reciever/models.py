from django.db import models

# Create your models here.
class Reciever(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	contact_no = models.CharField(max_length=11,null=True,blank=True)
	address = models.CharField(max_length=100,null=True,blank=True)


	def __str__(self):
		return self.first_name
