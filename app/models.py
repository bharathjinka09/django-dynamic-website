from django.db import models

# Create your models here.
class Post(models.Model):
	body = models.CharField(max_length=250)
	image = models.CharField(max_length=250)

	def __str__(self):
		return self.body

class CarouselImages(models.Model):
	image = models.CharField(max_length=250)

	def __str__(self):
		return self.image


class About(models.Model):
	about = models.TextField(max_length=500)

	def __str__(self):
		return self.about

class Contact(models.Model):
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
	address = models.TextField(max_length=500)

	def __str__(self):
		return self.email
		