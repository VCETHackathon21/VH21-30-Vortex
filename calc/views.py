from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def home(request):
    dest1 = Destination()
    dest1.name = 'Ajay Gupta'
    dest1.desc = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    dest1.img = "https://images.unsplash.com/photo-1614862876404-6866712b4a17?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80"
    dest1.price = 500

    dest2 = Destination()
    dest2.name = 'Vijay Gupta'
    dest2.desc = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    dest2.img = "https://images.unsplash.com/photo-1614597338748-e6dfa824a103?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=676&q=80"
    dest2.price = 700

    dest3 = Destination()
    dest3.name = 'Ranjana Gupta'
    dest3.desc = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    dest3.img = "https://images.unsplash.com/photo-1614863492516-34ddcb75beb2?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=676&q=80"
    dest3.price = 900

    dist = [dest1, dest2, dest3]
    return render(request , 'home.html' , {'data' : dist })


def addpost(request):
    return render(request , 'addpost.html')


def add(request):
    imgurl = request.POST['imgurl']
    username =  request.POST['username']
    desc =  request.POST['desc']
    title =  request.POST['title']
    
    return render(request , 'result.html' ,  { 'imgurl' : imgurl , 'title' : title ,'username' : username , 'desc' : desc })