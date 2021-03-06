from django.db import models
from pyuploadcare.dj.models import ImageField
from datetime import datetime

# Create your models here.
class Category(models.Model):
    Genre = models.CharField(blank=False, max_length=100)
    Tags = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.Genre
    class Meta:
        verbose_name_plural = "Categories"

class Games(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(blank=False, max_length=100)
    release_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    image = ImageField(blank=True, null=True)
    cost = models.FloatField(blank=False, )
   
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Games"
