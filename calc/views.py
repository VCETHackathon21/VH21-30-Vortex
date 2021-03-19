from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    dist = Destination.objects.all()
    return render(request , 'base.html' , {'data' : dist })

def login(request):
    return render(request , 'login.html')

def signup(request):
    return render(request , 'signup.html')


def loginpost(request):
    username = request.POST['username']
    password = request.POST['password']
    # Check and login 
    return redirect("/")


def signuppost(request):
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword'] 
    email = request.POST['email']
    firstname = username
    lastname = username

    # Craete new user here..

    if password == cpassword:
        if User.objects.filter(username=username).exists():
            # Redirect them to signup page
            messages.info(request , "Username Already Exist")
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            # Redirect them to signup page
            messages.info(request , "Email Is Already Taken")
            return redirect("/signup")
        else:
            user = User.objects.create_user(first_name=firstname , last_name=lastname, email=email, password=password, username=username)
            user.save()
            print("User created" , user)
            return redirect("/")
       
    else:
        messages.info(request , "Passwords does not match")
        return redirect("/signup")
     
    

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