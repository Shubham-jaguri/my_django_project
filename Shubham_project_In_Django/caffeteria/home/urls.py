from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.SignUp, name="SignUp"),
    path("signin", views.SignIn, name="signin"),
    path("logout", views.LogoutUser, name="logout"),
    path("ind", views.index1, name='index1'),
    path("menu",views.Menu, name="menu"),
    path("order", views.OrderMenu_Now, name='order'),
    path("table", views.Table_data, name='table'),
    path("search", views.Table_Search, name='search'),
    path("del/<int:id>/",views.Delete , name="delete"),
    path("update/<int:id>/",views.Update_Data, name="update"),
    path("upgra", views.Upgrade, name="upgrade"),
    path("contact", views.ContactUs, name="contact"),
    
]
