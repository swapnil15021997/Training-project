from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp1.models import ApplicationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from portal.models import profile,Forget_Password
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from functools import wraps
from django.db import DatabaseError,IntegrityError
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
import hashlib
from datetime import datetime,timedelta
import uuid
import secrets
from random import randint
# Create your views here.
from PIL import Image
def login_required(function=None, session_key='username'):
    def logindecorator(view_func):
        @wraps(view_func)
        def innerfunction(request, *args, **kwargs):
            if session_key in request.session:
                return view_func(request, *args, **kwargs)
            return redirect('login')
        return innerfunction
    if function is not None:
        return logindecorator(function)
    return logindecorator



def profile_view(request):
    
    current_user = request.session['username']
    
    data = profile.objects.filter(email=current_user).all()

    d1 = data.values()
   
    return render(request,'profile.html',{'data':d1})



@login_required
def AdminView(request):

    data = ApplicationForm.objects.all().count()
    student_data = ApplicationForm.objects.all()
    if 'username' in request.session:
        current_user = request.session['username']
        print(current_user)
        user_para = {'current_user': current_user}
        return render(request, 'index.html', {'data': data, 'student_data': student_data, 'user_para': user_para})
    else:
        return redirect('login')
@login_required
def Change_Pass_View(request):
    current_user = request.session['username']
    myuser = User.objects.get(username=current_user)
    print(myuser)
    
    if request.method == "POST":
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            old_password = request.POST['old_password']
            check = check_password(old_password, myuser.password)

            if check:
                pass1 = request.POST['new_password1']
                pass2 = request.POST['new_password2']
                if pass1 != pass2:
                # messages.warning(request,"Enter Correct Pass")
                    return JsonResponse({'status':'500','message':'Password doesnt match!'})
                else:
                    myuser.set_password(pass1)
                    myuser.save()
                    return redirect('login')
        # messages.warning(request,"Enter Correct Pass")
            return JsonResponse({'status':'500','message':'Please Enter Old Password Correctly!'})
    return render(request,'change-password.html')


def Change_Password(request):
   
    return render(request,'change-password.html')
@login_required
def edit_profile(request,id):
    current_user = request.session['username']
    data1 = profile.objects.filter(email=current_user).values()

    return render(request,'edit_profile.html',{'data1':data1})
@login_required
def Edit_Profile_View(request):
    current_user = request.session['username']
    data = profile.objects.filter(email=current_user).values()
    if request.method == "POST":
        try:
            im = request.FILES["image"]
        except:
            im = None
        
        id = request.POST.get('user_id') 
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile']       
        gender = request.POST['gender']       
        nationality = request.POST['nationality']
        updateRecords = {
            'first_name' :fname,
            'last_name':lname,
            'email':email,
            'mobile':mobile_number,
            'gender':gender, 
            'nationality':nationality,
            
        }

        if im !=None:
            updateRecords['profile_pic']=im
        else:
            messages.error(request, 'sorry, your image is invalid')

        get_user = User.objects.filter(username = current_user).values()
        user_data = {
           'first_name' :fname,
         'last_name':lname,
            'email':email,

         }
        
        get_user.update(**user_data)
        data.update(**updateRecords)
    return redirect('profile')

    


def DoRegistrationView(request):
    
    if request.method == "POST":
        first = request.POST['firstname']
        last = request.POST['lastname']
    
        try:
            im = request.FILES["image"]
        except:
            im = None
       # check if uploaded image is valid (for example not video file ) .
        if not im == None:
            try:
                Image.open(im)
            except:
                messages.error(request, 'sorry, your image is invalid')
        # uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['repass']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        address = request.POST['address']
        nationality = request.POST['Nationality']

        try:
            is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
            if User.objects.filter(username=email).exists():
                if is_ajax:
                    return JsonResponse({'status':'500','message':'User name already exist!'})
            user = User.objects.create_user(username=email, password=pass1)
            user.first_name = first
            user.last_name = last
            user.email = email
            user.passw = pass1
            user.is_staff = True
            user.save()
            data = profile(first_name=first, last_name=last,profile_pic=im, email=email,mobile=mobile,gender=gender,address=address,
            nationality=nationality,user=user)
            data.save()
            return JsonResponse({'status':'200','message':'User registration successful!'})
                    
        except DatabaseError:
            pass
            

def RegistrationView(request):    
    return render(request, 'register.html')


def LoginView(request):
    user = User.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        check_if_user_exists = User.objects.filter(username=username).exists()
        if check_if_user_exists:
            myuser = User.objects.get(username=username)
            if myuser is not None:
                check = check_password(password, myuser.password)
                if check:
                    request.session['username'] = username

                    return redirect('portal')
                else:
                    messages.warning(
                        request, "Wrong Password Please Enter Correct Password")
                    return redirect('login')
        else:
            messages.warning(request, "User not exist")
    return render(request, 'login.html')

@login_required
def logout_view(request):
    try:
        del request.session['username']
    except:
        return redirect('login')
    return redirect('login')


def Forget_pass_view(request):
    if request.method == "POST":
        email_id = request.POST['email']
        associated_user = User.objects.all().filter(username=email_id)
        id = associated_user.values('id')
        token = secrets.token_hex()     
        if associated_user.exists():
            Subject = "Request for Password Reset"
            text_template = "pass_reset.txt"
            uid=urlsafe_base64_encode(force_bytes(id))
            data = {

                "email": email_id,
                'domain':'127.0.0.1:8000',
				'site_name': 'Website',
                "uid": uid ,
				"user": associated_user,
				'token': token,
				'protocol': 'http',
            }


            myemail = render_to_string(text_template,data)

            email = EmailMessage(Subject, myemail, to=[email_id])
            email.send()
            time1 = datetime.now()+timedelta(minutes=5)
            

            unix_timestamp = datetime.timestamp(time1)*1000
            print(unix_timestamp)
            forget_pass_data = Forget_Password(email_id=email_id,status=False,token=token,timestamp=unix_timestamp)
        
            forget_pass_data.save()
            messages.success(request,"Password sent on Your email address")
        else:
            messages.warning(request,"Please Enter Valid Email Address !")
        
    return render(request,'forgot-password.html')




def reset_password(request,token):
    temp_timestamp = datetime.now()
    pass_reset_data = Forget_Password.objects.filter(token=token).values()
    email = pass_reset_data.values('email_id')[0]['email_id']
    status_code = pass_reset_data.values_list('status')[0][0]
    myuser = User.objects.get(username=email)
    exp_time = pass_reset_data.values_list('timestamp')[0][0]
    convert_exp  = float(exp_time) # exp time in data base
    print(status_code)
    unix_timestamp = datetime.timestamp(temp_timestamp)*1000

    convert_unix_timestamp = float(unix_timestamp)# current time 
    if pass_reset_data:
        if (convert_exp>convert_unix_timestamp) and (status_code==False):
            if request.method == "POST":
                
                pass1 = request.POST['new_password1']
                pass2 = request.POST['new_password2']
                if  pass1 == pass2:
                    myuser.set_password(pass1)
                    myuser.save()
                    data ={
                        'status':True
                    }
                    
                    pass_reset_data.update(**data)
                    return redirect('login') 
                
                else:
                
                    messages.warning(request,"Enter Correct Pass")
           
        else:
            return redirect('Forget_pass')
            
    else:
        messages.warning(request,"Enter Correct User Name")  
    return render(request,'pass_confirmation.html')


