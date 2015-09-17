from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.http import HttpUnauthorized

from tastypie.exceptions import BadRequest


from django.contrib import messages
from django.contrib.auth.models import User
from django.conf.urls import url
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


from reelio.utils import urlencodeSerializer
from login.forms import LoginForm, SignUpForm


class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['first_name', 'last_name', 'email']
        excludes = [ 'datetime']
        allowed_methods = ['get','post']
        serializer = urlencodeSerializer()
        
        
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout'),
            url(r'^(?P<resource_name>%s)/create%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('createUser'), name='api_create_user'),
        ]
    def createUser(self, request, **kwargs):        
        self.method_check(request, allowed=['post'])
        signupForm = SignUpForm(request.POST)
       
        if signupForm.is_valid():
                      
            userName = signupForm.clean_username()            
            userMail = signupForm.clean_username()
            signupForm = signupForm.clean()     
            password = signupForm['password']
            user = User.objects.create_user(userName, userMail, password)
            user.save()          
            user = authenticate(username=userName, password=password)                                     
            django_login(request,user)
            messages.success(request, "User account created succesfully")
            return self.create_response(request, {
                    'success': True
                })
        messages.error(request,signupForm.errors)
        raise BadRequest(signupForm.errors)
    def login(self, request, **kwargs):
        
        self.method_check(request, allowed=['post'])
        loginForm = LoginForm(request.POST)
        
        if loginForm.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')            
            user = authenticate(username=username, password=password)                
            if user is not None:                   
                django_login(request, user)
                messages.success(request, "Successfull logged in")
                return self.create_response(request, {
                    'success': True
                })
        messages.error(request,loginForm.errors)
        return self.create_response(request, {
                'success': False,
                'reason': loginForm.errors,
                }, HttpUnauthorized )
    def logout(self, request, **kwargs):       
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            messages.success(request, "You have been logged out.")
            django_logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)
        
        
    