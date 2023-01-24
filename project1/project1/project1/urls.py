"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from myapp1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('save',views.formSave, name="save"),
    path('',views.Home_View,name="home"),
    path('admission',views.Show_View,name="admission"),
    path('main/',views.Datatable_View, name='main'),
    path('main/<id>/', views.Student_details,name="details"),
    path("search/",views.search_field, name="search"),
    
    
    # UPdate
    path("search/user/edit/<id>",views.Edit_user_modal,name="edit-data"),
    path("search/update",views.Update_View, name="update"),
    
    path("search/delete",views.delete,name="delete"),    
    path("delete_view",views.Delete_View,name="delete_view"),

    #url for datatable
    
    path("json_data",views.Data_JSON,name="data-json-view"),

    


    path("data_list",views.Data_table_view,name="data-list-view"),


#for searching data in data table

    path("data/search",views.Search_in_Datatable,name="search_data_table"),

    path('portal/',include('portal.urls'))
]+ static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
