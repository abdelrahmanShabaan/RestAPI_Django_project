from django.shortcuts import render
from django.http import HttpResponse

from company.forms import EmployeeForm, EmployeeForm2, TeamForm, TeamForm2
from company.models import Employee, Team
from django.views.decorators.http import require_GET , require_POST ,require_http_methods
from django.views import View


# Create your views here.
def EmpolyeeView(request):

    if request.method == "GET":
        myform=EmployeeForm()
        return render(request, 'company/create_employee.html', {'form':myform})
    if request.method == "POST":
        myform=EmployeeForm(request.POST)
        if myform.is_valid():
        #  myform=EmployeeForm()
         team=Team.objects.filter(pk=request.POST['team'])[0]  
         Employee.objects.create(name=request.POST ['name'],
                                 salary=request.POST ['salary'],
                                 title=request.POST ['title'],
                                 team=team)
         return render(request, 'company/create_employee.html', {'form':myform})
    return HttpResponse("hi iti")


#--------------------------------- Lab Assignment Using First one ---------------------------------#
def TeamView(request):

    if request.method == "GET":
        myform=TeamForm()
        return render(request, 'company/create_team.html', {'form':myform})
    
    if request.method == "POST":
        myform=TeamForm(request.POST)
        # make valid
        if myform.is_valid():
        #  manager=Employee.objects.filter(pk=request.POST['empolyee'])[0]  
        #  Team.objects.create(name=request.POST ['name'], manager=manager)
         manager = myform.cleaned_data['manager']  # Use the correct field name here
         Team.objects.create(name=request.POST['name'], manager=manager)
         return render(request, 'company/create_team.html', {'form':myform})
    
    return HttpResponse("hi iti")
   



# Decorator (General constrant )
@require_http_methods(["GET" , "POST"])
def EmpolyeeView2(request):

    if request.method == "GET":
        myform=EmployeeForm2()
        return render(request, 'company/create_employee.html', {'form':myform})
    if request.method == "POST":
        myform=EmployeeForm2(request.POST)
        if myform.is_valid():
         myform.save()
        #  myform=EmployeeForm()
        #  team=Team.objects.filter(pk=request.POST['team'])[0]  
        #  Employee.objects.create(name=request.POST ['name'],
        #                          salary=request.POST ['salary'],
        #                          title=request.POST ['title'],
        #                          team=team)
         return render(request, 'company/create_employee.html', {'form':myform})
        

    return HttpResponse("hi iti")




# Decorator (General constrant )
@require_http_methods(["GET" , "POST"])
def TeamView2(request):

    if request.method == "GET":
        myform=TeamForm2()
        return render(request, 'company/create_team.html', {'form':myform})
    
    if request.method == "POST":
        myform=TeamForm2(request.POST)
        if myform.is_valid():
         myform.save()
        #  myform=EmployeeForm()
        #  team=Team.objects.filter(pk=request.POST['team'])[0]  
        #  Employee.objects.create(name=request.POST ['name'],
        #                          salary=request.POST ['salary'],
        #                          title=request.POST ['title'],
        #                          team=team)
         return render(request, 'company/create_team.html', {'form':myform})
        

    return HttpResponse("hi iti")




# ---------------------------------------------NEW-Using ClassView--------------------#
class EmployeeClassView(View):
   
    # Get Function
   def get(self,request):

    myform=EmployeeForm2()
    return render(request, 'company/create_employee.html', {'form':myform})

    # POST Function
   def post(self,request):
     
     myform=EmployeeForm2(request.POST)
     if myform.is_valid():
        myform.save()
     return render(request, 'company/create_employee.html', {'form':myform})



# ----------------------- Lab Requirement ------NEW-Class View-------------------#  
class TeamClassView(View):
   
    # Get Function
   def get(self,request):

    myform=TeamForm2()
    return render(request, 'company/create_team.html', {'form':myform})

    # POST Function
   def post(self,request):
     
     myform=TeamForm2(request.POST)
     if myform.is_valid():
        myform.save()
     return render(request, 'company/create_team.html', {'form':myform})