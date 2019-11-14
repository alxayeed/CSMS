from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	contact_no = models.CharField(max_length=11,null=True,blank=True)
	address = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.first_name


class Order(models.Model):
	order_id = models.CharField(max_length=8)
	sender_name = models.CharField(max_length=100)
	sender_contact = models.CharField(max_length=11)
	sender_address = models.TextField(max_length=100)
	sender_email = models.EmailField()
	order_area = models.CharField(max_length=20)

	reciever_name = models.CharField(max_length=100)
	reciever_contact = models.CharField(max_length=11)
	reciever_address = models.TextField(max_length=100)
	reciever_email = models.EmailField()

	product_name = models.CharField(max_length=50)
	product_type = models.CharField(max_length=20)
	product_quantity = models.BigIntegerField()
	product_weight = models.CharField(max_length=20)
	shipment_cost = models.IntegerField()
	payment_method = models.CharField(max_length=10)
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.product_name