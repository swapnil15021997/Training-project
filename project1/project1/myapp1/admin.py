from django.contrib import admin

# Register your models here.
from .models import ApplicationForm

@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ['reg_no','date','surname','name','fname','mname','adhar_no','dob','gender','place','city','dist','state','physical','schoolname']