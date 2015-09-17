# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.forms import HomeTasksForm
from home.models import HomeTasks
from django.http.response import HttpResponseRedirect



@login_required
def home(request):    
    tasks = HomeTasks.objects.filter(is_active = True, user = request.user)
    trashCount = HomeTasks.objects.filter(is_active = False,is_deleted = False, user = request.user).count()
    return render(request,"home/home.html",{'tasks':tasks,'trashCount':trashCount})

@login_required
def trashBox(request):    
    tasks = HomeTasks.objects.filter(is_active = False,is_deleted = False, user = request.user)
    trashCount = tasks.count()
    
    return render(request,"home/trash.html",{'tasks':tasks,'trashCount':trashCount})

@login_required
def create(request, id = None):
    
    try:
        task = HomeTasks.objects.get(id = int(id), user = request.user)
    except:
        if id is not None:
            return HttpResponseRedirect("/home/create/")
        else:
            task = None
    if task:
            taskForm = HomeTasksForm(instance = task)
    else:
            taskForm = HomeTasksForm()   
    return render(request,"home/create.html",{"taskForm":taskForm})
 