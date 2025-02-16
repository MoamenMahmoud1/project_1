from django.urls import path , include 
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    #path('about/<int:id>', views.contact, name='contact'),
    #path('about/<str:year>/', views.about_view, name='about_view'),
     path('about/special-path/', views.special_view, name='special-path'),
     path('about/add-ip/', views.add_ip_view, name='add-ip'),
     path('main/' , views.main , name='main'),
]
