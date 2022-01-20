from django.db import models

# Create your models here.
class Post(models.Model):
	body = models.CharField(max_length=250)
	image = models.CharField(max_length=250)

	def __str__(self):
		return self.body
