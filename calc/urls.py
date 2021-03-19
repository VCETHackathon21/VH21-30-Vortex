from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('addpost', views.addpost , name='addpost'),
    path('add' , views.add , name='add')
]