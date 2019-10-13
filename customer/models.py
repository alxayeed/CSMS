from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.first_name


class Order(models.Model):
	sender_name = models.CharField(max_length=100)
	sender_contact = models.CharField(max_length=11)
	sender_address = models.TextField(max_length=100)
	reciever_name = models.CharField(max_length=100)
	reciever_contact = models.CharField(max_length=11)
	reciever_address = models.TextField(max_length=100)
	product_quantity = models.IntegerField()
	shipment_cost = models.IntegerField()

	def __str__(self):
		return self.sender_name