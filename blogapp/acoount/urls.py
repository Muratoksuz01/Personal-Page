from django.urls import path
from . import views

urlpatterns=[ 
    path("login",views.Login_request,name="Login"),
    path("register",views.register_request,name="Register"),
    path("logout",views.Logout_request,name="Logout"),
    
    
    ]




