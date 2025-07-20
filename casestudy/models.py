from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    client = models.CharField(max_length=100, unique=True)

class Location(models.Model):
    location = models.CharField(max_length=100, unique=True)

class Industry(models.Model):
    industry = models.CharField(max_length=100, unique=True)

class Casestudy(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="casestudy_client")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_casestudy")
    description = models.TextField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="industry_casestudy")

    
