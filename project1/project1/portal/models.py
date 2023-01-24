from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class profile(models.Model):
    nation = (
           ('india','India'),
           ('pakistan','Pakistan'),
           ('nepal','Nepal'),
           ('bangladesh','Bangladesh')
       )
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="profile")
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField( max_length=50)
    nationality = models.CharField(choices = nation,max_length=50)
    passw = models.CharField( max_length=50)

    def update(self,*args, **kwargs):
        for name,values in kwargs.items():
            try:
                setattr(self,name,values)
            except KeyError:
                pass
        self.save()
    

class Forget_Password(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.ManyToManyField(User)
    email_id = models.EmailField()
    status = models.BooleanField()
    token = models.CharField(max_length=150)
    timestamp = models.CharField(max_length=100)
    def update(self,*args, **kwargs):
        for name,values in kwargs.items():
            try:
                setattr(self,name,values)
            except KeyError:
                pass
        self.save()
    