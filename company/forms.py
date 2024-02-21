from django import forms

from company.models import Employee, Team


#------------------------------ First Way of Model.forms.Form ----------------------------#
class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=50)
    salary=forms.IntegerField()
    title=forms.CharField(max_length=50)
    team=forms.ChoiceField(choices=[(team.pk,team.pk)for team in Team.objects.all()], required=False)
    
    # Additional edit or addational if i want to add
    # team_name=forms.CharField(max_length=30)
    # manager=forms.CharField(max_length=30)



#------------------------------  Second Way of Model.ModelForm ------------------------------#
class EmployeeForm2(forms.ModelForm):
    # if i want to change constrains 
    # salary=forms.CharField(max_length=20) 
     class Meta:
          model= Employee
          fields="__all__"
    #if i want to get some thing specific
        # fields=["name" , "salary"]
        #   exclude=["name"]
          
        

# ---------------------------------------- Lab Requirements First Way of Model.forms.Form  (Team) --------------------------------#
class TeamForm(forms.Form):
     name=forms.CharField(max_length=50)
    #  manager=forms.ForeignKey(Employee,on_delete=forms.PROTECT,related_name="team_manager")
    #  manager=forms.ChoiceField(choices=[(manager.pk,manager.pk)for manager in Employee.objects.all()], required=False)
     manager = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)





#------------------------------   Lab Requirements  Second Way of Model.ModelForm  (Team) ------------------------------#
class TeamForm2(forms.ModelForm):
     class Meta:
          model= Team
          fields="__all__"
        #   exclude=["name"]