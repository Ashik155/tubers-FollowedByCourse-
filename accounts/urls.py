from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path("login_page", views.login_page, name='login_page'),
    path("register", views.register, name='register'),
    path("logout_user", views.logout_user, name='logout_user'),
    path("dashboard", views.dashboard, name='dashboard'),
    
    


]