from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('login1/', views.login_view, name='login1'),
    path('signup1/', views.signup_view, name='signup'),
    path('logout1/', views.logout_view, name='logout'),
]
