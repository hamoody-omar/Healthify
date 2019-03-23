from django.urls import path, include
from . import views

urlpatterns = [
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_make_appointment', views.make_appointment,
         name='user_make_appointment'),
    path('user_view_appointments', views.user_view_appointments,
         name='user_view_appointments'),
    path('user_view_med_his', views.view_med_his, name='user_view_med_his'),
    path('user_get_coverage', views.get_coverage, name='user_get_coverage'),



]
