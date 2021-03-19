from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def home(request):
    dist = Destination.objects.all()
    return render(request , 'base.html' , {'data' : dist })


def addpost(request):
    return render(request , 'addpost.html')


def add(request):
    imgurl = request.POST['imgurl']
    username =  request.POST['username']
    desc =  request.POST['desc']
    title =  request.POST['title']
    
    data1 = Destination(imgurl = imgurl , username = username ,  desc = desc, title = title)
    data1.save()

    return redirect("/")
    # return render(request , 'result.html' ,  { 'imgurl' : imgurl , 'title' : title ,'username' : username , 'desc' : desc })