from django.db import models

# Create your models here.
class Shop_data(models.Model):
    name= models.CharField(max_length=50)
    brand= models.CharField(max_length=50)
    price= models.IntegerField()
    slug= models.CharField(max_length=50)
    # slu= models.CharField(max_length=50)
 