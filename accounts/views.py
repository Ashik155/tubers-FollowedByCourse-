from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate( username = username)
        print(user)
        print("user from db", User.objects.filter(username=username, password=password))
        print("user is fetched from DB")
        if user is not None:
            print("user found")
            
            auth.login(request, user)
            messages.success(request, "Logged innnnn")
            redirect('dashboard')

        else:
            print("user not found ")
            messages.error(request, 'Ooops, wrong credentials, plaese try again')
            return redirect('login_page')


     
    return render(request, 'accounts/login.html')


def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST["last_name"]
        user_name = request.POST['user_name']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if(password == confirm_password):
            if(User.objects.filter(username=user_name).exists()):
                messages.error(request, "haha, already exist ! Why dont you login")
                return redirect('register')
            else:
                if(User.objects.filter(email=email).exists()):
                    messages.error(request, 'Ooops, Email is already in use, choose another one ')
                    return redirect('register')
                else:
                    user = User.objects.create(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password)
                    user.save()
                    messages.success(request,'Heya'+first_name+" your account has been created successfully.. ")
                    return redirect('login_page')
        else:
            messages.error(request, 'Sorry I think you have entered wrong Password')
            return redirect('register')
    
    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')