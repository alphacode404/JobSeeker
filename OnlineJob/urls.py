from django.urls import path
from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('applied', views.jobresults, name="applied"),

    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('register', views.register, name="register"),

    path('company', views.company, name="company"), 
    path('jobdetail/<int:job_id>/', views.jobdetial, name="jobdetail"),
    path('profile', views.profile, name='profile'),
    path('cv', views.cv, name='cv'),

    path('note', views.note, name='note'),
    path('noteupdate', views.noteupdate, name='noteupdate'),
    path('notedelete/<str:pk>', views.notedelete, name='notedelete'),

    path('applicantstatus', views.applicantstatus, name='applicantstatus'),
  
    
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='pages/user-profile.html ', success_url='/'), name='change-password'),

    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='passwordconfig/password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetView.as_view(template_name="passwordconfig/password_reset_sent.html"), name='password_reset_done'),

    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name='passwordconfig/password_reset_done.html'), name='password_reset_complete'),
]
