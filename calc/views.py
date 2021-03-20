from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination, Tag
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    datatags = []
    dist = Destination.objects.all()
    for data in dist:
        alltags = Tag.objects.filter(isrelated=data.id)
        datatags.append(alltags)

    return render(request , 'base.html' , {'data' : dist , 'datatags' : datatags  })

def login(request):
    return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def signup(request):
    return render(request , 'signup.html')


def loginpost(request):
    username = request.POST['username']
    password = request.POST['password']
    # Check and login 
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        print("User is logged in")
        return redirect("/")
    else:
        messages.info(request , "Something went wrong")
        return redirect("/login")


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
            auth.login(request , user)
            print("User created" , user)
            return redirect("/")
       
    else:
        messages.info(request , "Passwords are not matching..")
        return redirect("/signup")
     
    
def addpost(request):
    dist = Destination.objects.all()
    return render(request , 'addpost.html' , {'data' : dist })


def add(request):
    isanonymous = False
    if request.POST.get('isanonymous' , None):
        print("isanonymous =-==> truesfef")
        isanonymous = True

    imgurl = request.POST['imgurl']
    desc =  request.POST['desc']
    title =  request.POST['title']
    alltags = request.POST['tags']
    alltagslst = alltags.split()

    if request.user:
        if isanonymous:
            data1 = Destination(imgurl = imgurl ,  desc = desc, title = title)
        else:
            data1 = Destination(imgurl = imgurl , author=request.user, desc = desc, title = title)
    else:
        data1 = Destination(imgurl = imgurl, desc = desc, title = title)

    data1.save()
    for data in alltagslst:
        newtag = Tag(name=data, isrelated=data1)
        newtag.save()
   
    return redirect("/")