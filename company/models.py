from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    title=models.CharField(max_length=50)
    team=models.ForeignKey("Team" ,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    


class Team(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    manager=models.ForeignKey(Employee,on_delete=models.PROTECT,related_name="team_manager")
 
    def __str__(self):
        return self.name
