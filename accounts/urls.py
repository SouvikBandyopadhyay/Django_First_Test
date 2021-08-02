from django.urls import path
from . import views

urlpatterns = [
    path("register",views.addaccount,name="register"),
    path("login",views.enteraccount,name="login"),
    path("logout",views.exitaccount,name="logout"),
    
]