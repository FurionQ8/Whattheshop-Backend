from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	painting = models.CharField(max_length = 120)
	description = models.TextField()
	artist = models.CharField(max_length = 120)
	year = models.IntegerField(max_length = 4)
	image = models.ImageField(null =True , blank = True)
	price = models.DecimalField(max_digits = 8 , decimal_places = 2)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return self.painting

class Cart(models.Model):
	name = models.CharField(max_length=100)

class Location(models.Model):
	area = models.CharField(max_length=50)
	block = models.IntegerField()
	street = models.CharField(max_length=50)
	cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username