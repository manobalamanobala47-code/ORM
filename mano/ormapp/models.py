from django.db import models
from django.contrib import admin
class car(models.Model):
    model=models.IntegerField()
    cname=models.CharField(max_length=100)
    price=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('model','cname','price','year','rating')


