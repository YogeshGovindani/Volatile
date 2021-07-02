from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Contest
# Create your views here.


def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(request.user.username)
            return redirect("/")
        else:
            message = "User doesnt exist"
            return render(request, "login.html", {
                "message": message
            })
    return render(request, "login.html", {
        "message": ""
    })


def signup(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        print(username, email, password)
        user = User.objects.create_user(
            username=username, email=email, password=password)
        return redirect("/login")
    return render(request, "signup.html")


@login_required(login_url="/login")
def home(request):
    contest_list = Contest.objects.all()
    return render(request, "home.html", {
        "contest_list": contest_list
    })


# Getting Error
def logout(reuest):
    auth_logout(request)
    return redirect("/login")
