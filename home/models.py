from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class HomeTasks(models.Model):   
    user = models.ForeignKey(User)   
    title = models.CharField(max_length = 200)
    summary = models.TextField(blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_deleted = models.BooleanField(default = False)
    datetime = models.DateTimeField(auto_now_add=True)
    
    
    