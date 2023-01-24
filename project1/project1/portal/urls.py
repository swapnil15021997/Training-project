from django.urls import path,include
from portal import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
urlpatterns = [
    path('', views.AdminView, name='portal'),
    path('registration/', views.RegistrationView,name='registration'),
    path('do-registration/', views.DoRegistrationView,name='do-registration'),
    path('login',views.LoginView,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('profile',views.profile_view,name='profile'),
    path('user/change_pass',views.Change_Password,name='change_password'),
    path('user/change_pass_view',views.Change_Pass_View,name='Change_Pass_View'),

    path('user/forgot_pass',views.Forget_pass_view,name='Forget_pass'),
    path('user/reset_password/<slug:token>',views.reset_password,name='reset_password'),

  
    

    path('user/edit_userdata',views.Edit_Profile_View,name='edit_data'),
    path('portal/edit_profile/<id>',views.edit_profile,name='edit_profile'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)