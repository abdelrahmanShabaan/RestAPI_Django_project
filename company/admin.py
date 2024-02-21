from django.contrib import admin

from company.models import Employee, Team


# Register your models here.

admin.site.register(Employee)
admin.site.register(Team)