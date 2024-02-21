from django.shortcuts import render
from django.http import HttpResponse
from company.forms import EmployeeForm
from company.models import Employee, Team

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