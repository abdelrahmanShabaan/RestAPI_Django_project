"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from company.views import EmpolyeeView , EmpolyeeView2 ,EmployeeClassView ,TeamView ,TeamView2 ,TeamClassView



from myapi.views import EmployeesFunBaseView,EmployeesFunBaseView2,EmployeesFunBaseView3 ,TeamFunBaseView ,TeamFunBaseView2 ,TeamFunBaseView3

from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
#------------------Lecture way to make---------------------------------#
router.register(r'', EmployeesFunBaseView3, basename='employees-all-3')
#-----------------Lab Develop---------------------------------#
router.register(r'', TeamFunBaseView3, basename='teams-all-3')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",EmpolyeeView ,name="EmpolyeeView"),
    path("emp/",EmpolyeeView2 ,name="EmpolyeeView2"),
    path("EmployeeClassView/",EmployeeClassView.as_view() ,name="EmployeeClassView"),
    path("TeamView/",TeamView ,name="TeamView"),
    path("TeamView2/",TeamView2 ,name="TeamView2"),
    path("TeamClassView/",TeamClassView.as_view() ,name="TeamClassView"),

    # Configrations of the RESTAPIS
    path('api-auth/', include('rest_framework.urls')),

    path('employees-all/',EmployeesFunBaseView,name="employees-all"),
    path('employees-all-2/',EmployeesFunBaseView2.as_view(),name="employees-all-2"),
    path('employees-all-3/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))


#------------------------Way of Lab ---------------------------------------------------#
    path('teams-all/',TeamFunBaseView,name="teams-all"),
    path('teams-all-2/',TeamFunBaseView2.as_view(),name="teams-all-2"),
    path('teams-all-3/', include(router.urls)),




]
