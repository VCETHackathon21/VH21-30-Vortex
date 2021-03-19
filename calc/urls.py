from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('addpost', views.addpost , name='addpost'),
    path('add' , views.add , name='add'),
    path('login', views.login,  name='login'),
    path('signup' , views.signup , name='signup'),
    path('signuppost', views.signuppost, name="signuppost"),
    path('loginpost', views.loginpost , name="loginpost")
]