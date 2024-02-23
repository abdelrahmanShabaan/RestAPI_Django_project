from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from company.models import Employee, Team
from myapi.serializers import EmployeeSerializer, TeamSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["GET", "POST"]) #Decorator
def EmployeesFunBaseView(request):
    
    if request.method == 'GET':
        employees=Employee.objects.all() # GET All Data from model 
        seralizer=EmployeeSerializer(employees,many=True) # use Serilzier with many for more data
        return Response(seralizer.data) # get response with json Data
    
    if request.method == 'POST':
        data=request.data # Instead .POST
        seralizer=EmployeeSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save() # Create Emolyee with data 
            return Response(status=status.HTTP_201_CREATED)  # Get Success with status Create
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
class EmployeesFunBaseView2(APIView):
    
    def get(self,request):
        employees=Employee.objects.all()  # GET All Data from model 
        seralizer=EmployeeSerializer(employees,many=True) # use Serilzier with many for more data
        return Response(seralizer.data) # get response with json Data
    
    def post(self,request):
        data=request.data
        seralizer=EmployeeSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()  # Create Emolyee with data 
            employees=Employee.objects.all()
            all_data=EmployeeSerializer(seralizer.data) 
            return Response({"emplyees":all_data.data},status=status.HTTP_201_CREATED) # Get Success with status Create
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        

class EmployeesFunBaseView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]  # check if Actual Authentications
    permission_classes = [IsAuthenticated]          # check if the permission access
    serializer_class = EmployeeSerializer           # make serializer class = Modul Serializer
    queryset = Employee.objects.all()




#-------------------------------------------LAB Requiremens-----------------------------------#

@api_view(["GET", "POST"]) #Decorator
def TeamFunBaseView(request):
    
    if request.method == 'GET':
        team=Team.objects.all() # GET All Data from model 
        seralizer=TeamSerializer(team,many=True) # use Serilzier with many for more data
        return Response(seralizer.data) # get response with json Data
    
    if request.method == 'POST':
        data=request.data # Instead .POST
        seralizer=TeamSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save() # Create Emolyee with data 
            return Response(status=status.HTTP_201_CREATED)  # Get Success with status Create
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




# @api_view(["GET", "POST"]) Because i have actual GET & POST
class TeamFunBaseView2(APIView):
    
    def get(self,request):
        team=Team.objects.all()  # GET All Data from model 
        seralizer=TeamSerializer(team,many=True) # use Serilzier with many for more data
        return Response(seralizer.data) # get response with json Data
    
    def post(self,request):
        data=request.data
        seralizer=TeamSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()  # Create Emolyee with data 
            team=Team.objects.all()
            all_data=TeamSerializer(seralizer.data) 
            return Response({"emplyees":all_data.data},status=status.HTTP_201_CREATED) # Get Success with status Create
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        




class TeamFunBaseView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] # check if Actual Authentications
    permission_classes = [IsAuthenticated]         # check if the permission access
    serializer_class = TeamSerializer              # make serializer class = Modul Serializer
    queryset = Team.objects.all()

