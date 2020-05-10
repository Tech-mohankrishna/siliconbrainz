from django.db import models
from datetime import datetime

# Create your models here.

class PicturesCategory(models.Model):
    pictures_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

class Meta:
    verbose_name_plural = "Categories"

def __str__(self):
    return self.pictures_category

class PicturesSeries(models.Model):
    pictures_series = models.CharField(max_length=200)
    pictures_category = models.ForeignKey(PicturesCategory, default= 1 , verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

class Meta:
    verbose_name_plural = "Series"

def __str__(self):
    return self.pictures_series


class pictures(models.Model):   
    pictures_title = models.CharField(max_length=200)
    pictures_content = models.TextField()
    pictures_published = models.DateTimeField("date published",default = datetime.now())
    pictures_thumb = models.ImageField(default='default.png', blank=True)

    pictures_series = models.ForeignKey(PicturesSeries, default= 1 , verbose_name= "Series", on_delete=models.SET_DEFAULT)
    pictures_slug = models.CharField(max_length=200, default=1)


def __str__(self):
    return self.pictures_title
        
