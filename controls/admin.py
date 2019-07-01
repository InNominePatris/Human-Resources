from django.contrib import admin
from .models import AttendanceRequest


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('status', 'employee', 'from_date', 'to_date')
    search_fields = ['employee', 'status']


admin.site.register(AttendanceRequest, AttendanceAdmin)