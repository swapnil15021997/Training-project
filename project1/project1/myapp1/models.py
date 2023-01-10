from django.db import models
from datetime import datetime, date
# Create your models here.
class ApplicationForm(models.Model):
    reg_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to = 'profile')



    
    date = models.DateField(null=True,auto_now_add=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    fname = models.CharField(max_length=50)
    mname =  models.CharField(max_length=50)
    adhar_no = models.IntegerField()
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dist = models.IntegerField()
    state_choice = (
           ('maharashtra','Maharashtra'),
           ('gujrat','Gujrat'),
           ('Rajasthan','Rajasthan')
       )
    state = models.CharField(choices=state_choice, max_length=50)
    physical_state = (
        ('Yes','Yes'),
        ('No','No')
    )
    physical = models.CharField(choices=physical_state, max_length=50)
    schoolname = models.CharField(max_length=50)