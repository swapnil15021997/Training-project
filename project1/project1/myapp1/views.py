from django.shortcuts import render
from django.http import HttpResponse
from .models import ApplicationForm
from datetime import datetime
# Create your views here.
from django.views.generic import DetailView

def formSave(request):
    
    if request.method == "POST":
        reg = request.POST['regno']
        
        im = request.FILES['image']
        dt = request.POST['date']
        
        # dt = datetime.strptime(dt, "%d/%m/%Y").strftime("%Y-%m-%d")

        
        sname = request.POST['surname']
        nm = request.POST['name']
        fn = request.POST['fname']
        mn = request.POST['mname']
        ad = request.POST['adno']
        db=request.POST['dob']
       

        gen= request.POST['gender']

        pl= request.POST['place']

        dt= request.POST['dist']
        st= request.POST['State']
        phy= request.POST['physical problems']

        school= request.POST['schoolname']
        data = ApplicationForm(reg_no = reg,surname=sname,name=nm,fname=fn,mname=mn, adhar_no =ad, 
        gender=gen,place = pl,dist=dt,state=st,physical=phy,schoolname=school,date = dt,dob=db,profile_pic=im)
        data.save()
        #,dob=db,
        return HttpResponse("<h1>Hello Data saved Successfully<h1>")
    return render(request,'application.html')


def Show_View(request):
    data = ApplicationForm.objects.all()
    return render(request, 'details.html',{'data':data})


def Index_View(request):
    data = ApplicationForm.objects.all().count()
    student_data = ApplicationForm.objects.all()
    print("Total entries",data)
    return render(request, 'index.html',{'data':data, 'student_data':student_data})

def Base_View(request):
    return render(request, 'base.html')

def Datatable_View(request):
    data = ApplicationForm.objects.all()
    return render(request, 'data-tables.html',{'data':data})


# class Student_details(DetailView):
#     model = ApplicationForm
#     template_name = 'details.html'

def Student_details(request, id):
    data = ApplicationForm.objects.get(id=id)
    print(data)
    return render(request,'details.html', {'data':data})


