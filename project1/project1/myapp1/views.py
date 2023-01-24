from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ApplicationForm
from django.views.generic import DetailView
from django.http import JsonResponse
from PIL import Image
from django.core import serializers
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from portal.views import login_required
import json
from datetime import datetime 
from django.db.models import Q


# Create your views here.


@login_required
def formSave(request):
    if request.method == "POST":
        reg = request.POST['regno'] #regno name is same on html field
        try:
            im = request.FILES["image"]
        except:
            im = None
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
       # check if uploaded image is valid (for example not video file ) .
        if not im == None:
            try:
                Image.open(im)
            except:
                if is_ajax:
                    return JsonResponse({'status':'500','message':'Invalid image    !'})
                else:
                    # messages.error(request, 'sorry, your image is invalid')
                    return redirect('save')
        dt = request.POST['date']
        sname = request.POST['surname']
        nm = request.POST['name']
        fn = request.POST['fname']
        mn = request.POST['mname']
        ad = request.POST['adno']
        db=request.POST['dob']
        cty = request.POST['city']
        gen= request.POST['gender']
        pl= request.POST['place']
        dist= request.POST['dist']
        st= request.POST['State']
        phy= request.POST['physical problems']
        school= request.POST['schoolname']
        data = ApplicationForm(reg_no = reg,surname=sname,name=nm,fname=fn,mname=mn, adhar_no =ad, 
        gender=gen,place = pl,dist=dist,state=st,physical=phy,schoolname=school,date=dt,dob=db,profile_pic=im,city=cty)
        data.save()
        return JsonResponse({'status':'200','message':'Saved successfully!'})
    return render(request,'admission-form.html')

@login_required
def Show_View(request):
    data = ApplicationForm.objects.all()
    return render(request, 'admission-form.html')


def Home_View(request):
    return render(request, 'login.html')

@login_required
def Datatable_View(request):
    data = ApplicationForm.objects.all()
    per_page= 5
    obj_data = Paginator(data,per_page) #it tells how much data show per page
    first_page = obj_data.page(1).object_list
    last_page = obj_data.page_range
    context = {
        'obj_data':obj_data,
        'first_page':first_page,
        'last_page':last_page,
        'data':data
    }  
    if request.method == 'POST':
        #getting page number
        page_no = request.POST.get('page_no', None) 
        results = list(obj_data.page(page_no).object_list.values('id','reg_no','date','surname','fname','name','adhar_no','mname','gender','place','city','dist','state','state','physical','schoolname',))
        return JsonResponse({"results":results})
    return render(request, 'data-tables.html',context)


@login_required
def search_field(request):
    if request.method =="POST":
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax: 
            nam= request.POST.get('search_text') 
            name_list = ApplicationForm.objects.filter(name__startswith=nam).values()  
            return JsonResponse({'status':'200','message':'Ok!','users':list(name_list)}) 
    return render(request,'search.html')


@login_required
def Student_details(request, id):
    data = ApplicationForm.objects.get(id=id)
    return render(request,'details.html', {'data':data})




@login_required    
def Update_View(request):
    if request.method == "POST":
        try:
            im = request.FILES["image"]
        except:
            im = None
        
        id = request.POST.get('user_id') 
        print(id)
        reg = request.POST['regno']
        dt = request.POST['date_reg']
        db=request.POST['dob']
       
        sname = request.POST['surname']
        nm = request.POST['name']
        fn = request.POST['fname']
        mn = request.POST['mname']
        ad = request.POST['adno']
        
        cty = request.POST['city']
        gen= request.POST['gender']
        print(gen)
        pl= request.POST['place']
        dist= request.POST['dist']
        st= request.POST['State']
        phy= request.POST['physical problems']
        school= request.POST['schoolname']

        # d = {"num_pages":40, author:"Jack", date:"3324"}
        updateRecords = {
            'reg_no' :reg,
            'surname':sname,
            'name':nm,
            'fname':fn,
            'mname':mn, 
            'adhar_no' :ad, 
            'gender':gen,
            'place' : pl,
            'dist':dist,
            'state':st,
            'physical':phy,
            'schoolname':school,
            'date':dt,
            'dob':db, 
            'city':cty
        }

        if im !=None:
            updateRecords['profile_pic']=im


        user = ApplicationForm.objects.get(id = id)
        print(user)
        user.update(**updateRecords)
        return redirect('search')



def Edit_user_modal(request,id):
    data = ApplicationForm.objects.get(id=id)
    
    return render(request,'update.html',{'data':data})


def Delete_View(request):
    if request.method == "POST":
        id1 = request.POST.get(id)
        print(id1)
        data = ApplicationForm.objects.get(id = id1)
        data.delete()
        return HttpResponse('deleted')
   

def delete(request):

    if request.method == "POST":
        id1 = request.POST.get('id')
        
        data = ApplicationForm.objects.get(id = id1)
        print(data)
        data.delete()
        return redirect('search.html')
    return HttpResponse('deleted')


#JSON RESPONSE

def Data_JSON(request):
    
    search = str(request.GET["search[value]"])
    
    offset = int(request.GET['start'])

    limit = int(request.GET['length'])    
    count   =   ApplicationForm.objects.count()
    
    records =   ApplicationForm.objects.all().order_by('name')[offset:limit+offset]
   
    limit = limit+offset

    # CODE FOR SORTING 
    col = int(request.GET['order[0][column]'])
    sort = str(request.GET['order[0][dir]'])
    columns = ['id','name','surname']
    sortable_col = str(columns[col])
    
    


    
   
    

    if search =="":
        if sort=="asc":
            sorted_data = ApplicationForm.objects.order_by(sortable_col)[offset:limit+offset]
            
        else:
            sorted_data = ApplicationForm.objects.order_by(sortable_col).reverse()[offset:limit+offset]

        # all_data =  [records.get_data() for records in records ]
        all_data =  [sorted_data.get_data() for sorted_data in sorted_data ]
        print("You are in if")

        all_records = {
            "recordsTotal": count,  
            "recordsFiltered":count, 
            "data": all_data,    
         }
        
        return JsonResponse(all_records,safe=False,content_type = "application/json")
    else:
        
        data = ApplicationForm.objects.filter(Q(name__icontains=search) | Q(surname__icontains=search)).order_by('name')[offset:limit]
        q_data = [data.get_data() for data in data ]
       
        records = {
            "recordsTotal": count,    # The total count of records in your database, if query exist, it is the count of filtered records
            "recordsFiltered":count,
            "data": q_data,    # Main data to be rendered in table
         }
         
        return JsonResponse(records,safe=False,content_type = "application/json")

       
    # else:
    #     print("blank")
    #             # data = records.get_queryset().values()
    #     all_data =  [records.get_data() for records in records ]
    #     print(all_data)

    #     all_records = {
    #         "recordsTotal": count,  
    #         "recordsFiltered":count, 
    #         "data": all_data,    
    #      }
        
    #     return JsonResponse(all_records,safe=False,content_type = "application/json")
      
    


#HTML RENDER


def Data_table_view(request):
    return render(request,'data_tab.html')
    
def sorting(col,sort):
    
    
    pass

def Search_in_Datatable(request):
   
    return HttpResponse("<h5> Hello </h5> ")

        
   