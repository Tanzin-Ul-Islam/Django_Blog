from django.contrib import admin
from django.urls import path
from blog_app import views


app_name='blog_app'


urlpatterns = [

    path('',views.bloglist.as_view(),name='blog_list'),
    path('write_blog/',views.createblog.as_view(),name='createblog'),
    path('details/<str:slug>', views.blog_details, name='blog_details'),
    path('myblogs/', views.myblogs.as_view(), name='myblogs'),
    path('like/<pk>', views.liked, name='like'),
    path('dislike/<pk>', views.disliked, name='dislike'),
    path('editblog/<pk>', views.editblog.as_view(), name='editblog'),

]