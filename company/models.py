from django.db import models

# Create your models here.
class Empolyee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.models.IntegerField()
    title=models.CharField(max_length=50)