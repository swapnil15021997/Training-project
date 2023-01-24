from django.db import models

from datetime import datetime, date
# Create your models here.
class ApplicationForm(models.Model):
    reg_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to = 'profile')
    date = models.DateField(blank=True, null=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    fname = models.CharField(max_length=500)
    mname =  models.CharField(max_length=50)
    adhar_no = models.IntegerField()
    dob = models.DateField(blank=True)

    Gender_Choice = (
    ('male','Male'),
    ('female','Female')
    )
    gender = models.CharField(max_length=50, choices=Gender_Choice)

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


    def update(self,*args, **kwargs):
        for name,values in kwargs.items():
            try:
                setattr(self,name,values)
            except KeyError:
                pass
        self.save()

    def get_data(self):
        return{
            "id":self.id,
            "name":self.name,
            "surname":self.surname
        }