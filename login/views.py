
# Create your views here.
from login.forms import LoginForm, SignUpForm
from django.shortcuts import HttpResponseRedirect, render

def login(request):    
    if request.user.is_anonymous():
        loginForm = LoginForm()
        return render(request,"login/login.html",{"loginForm":loginForm})
    else:
        return HttpResponseRedirect("/home/")

def signup(request):
    if request.user.is_anonymous():
        signupForm = SignUpForm()
        return render(request,"login/signup.html",{"signupForm":signupForm})
    else:
        return HttpResponseRedirect("/home/")