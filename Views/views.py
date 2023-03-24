from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from Views.forms import UserRegistration, LoginForm, BooksForm
from Models.models import Books
from django.http import FileResponse
import os
# Create your views here.


def index(request):
    items = {
        'form' : BooksForm(request.GET)
    }
    return render(request, "Views/index.html", context = items)


def registration(request):
    items = {
        "form" : UserRegistration(request.GET),
        
    }
    return render(request, "Views/register.html", context = items)

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["confirm_password"]

            if password == password2:
                user = User.objects.create_user(username = username, password = password)
                return HttpResponse("User Registered Successfully")
            
            else:
                return HttpResponse("Password Doesn't Match")
        return HttpResponse("Invalid / Bad Form")
    

def login(request):
    items = {
        'form' : LoginForm()
    }
    return render(request, "Views/login.html", context = items)

def login_user(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            user_login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid Username / Password")
    else:
        print(form.errors)
        return HttpResponse("Invalid Form")
    


def search_title(request):
    form = BooksForm(request.POST)


    if form.is_valid():
        title = form.cleaned_data["title"]
        result = Books.objects.filter(title__icontains = title)
        print(result)
        items = {
            'titles' : result
        }
        return render(request, 'Views/search_result.html', context = items)
    else:
        return HttpResponse("Invalid Form")
    


def view_book(request):
    return render(request, "Views/view.html" )


def download(request):

    return FileResponse(open(f'{os.getcwd()}{request.GET.get("filename")}', 'rb'))



