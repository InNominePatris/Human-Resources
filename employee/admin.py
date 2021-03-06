from django.contrib import admin
from .models import Employee, AcademicStudies, Relative


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name', 'identity']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(AcademicStudies)
admin.site.register(Relative)


