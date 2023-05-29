from django.db import models

# Create your models here.
class tbl(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    email=models.EmailField()
