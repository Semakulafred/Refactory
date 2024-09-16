from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from pages import views

def user_login(request):
    # if not request.user.is_authenticated:
    #     if request.method == 'POST':
    #         username = request.POST['username']
    #         password = request.POST['password']

    #         user = auth.authenticate(username=username, password=password)

    #         if user :
    #             auth.login(request, user)
    #             if request.GET.get(next, None):
    #                  return HttpResponseRedirect(request.GET[None])
    #             return redirect(views.homePage)
    #         else:
    #             messages.info(request, 'Invalid Login Info')
    #         return render(request, 'authentication/login.html', {})
    #     else:
    #         return render(request, 'authentication/login.html', {})
    # else:
    #     return redirect('')
    return render(request, 'authentication/login.html', {})

def register(request):
    if request.method =='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirmpassword']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists!')
                return render(request, 'authentication/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists!')
                return render(request, 'authentication/signup.html')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Successfully Created A profile')
                return redirect(user_login)
    else:
         messages.info(request, 'Password Not Matching')
         return render(request, 'authentication/signup.html')
    return render(request, 'authentication/signup.html')
