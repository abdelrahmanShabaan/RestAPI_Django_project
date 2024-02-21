from django.db import models

# Create your models here.
class Empolyee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    title=models.CharField(max_length=50)


class Team(models.Model):
    name=models.CharField(max_length=50)
    manager=models.ForeignKey(Empolyee,on_delete=models.PROTECT)
