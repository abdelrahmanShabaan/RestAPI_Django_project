from django.shortcuts import render
from django.http import HttpResponse
from company.models import Employee

# Create your views here.




def EmpolyeeView(request):
    print(Employee.objects.filter(team='IT'))

    return HttpResponse("hi iti")