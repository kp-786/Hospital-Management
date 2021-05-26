from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('',views.home, name='home'),
    path('aboutus/',views.about_us, name='about_us'),
    path('contact/',views.contact, name='contact'),
]