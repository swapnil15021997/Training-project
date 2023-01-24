from django.contrib import admin
from portal.models import profile,Forget_Password
# Register your models here.

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email','passw','profile_pic','mobile','gender','address','nationality']

@admin.register(Forget_Password)
class Forget_PasswordAdmin(admin.ModelAdmin):
    list_display=['email_id','status','token','timestamp']