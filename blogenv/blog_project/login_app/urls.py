from django.contrib import admin
from django.urls import path
from login_app import views


app_name='login_app'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('password/', views.updatepass, name='updatepassword'),
    path('uploadpic/', views.uploadprofilepic, name='uploadpic'),
    path('changepic/', views.changeprofilepic, name='changepic'),

]
