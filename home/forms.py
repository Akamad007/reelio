'''
Created on Jul 18, 2015

@author: akash
'''


from django import forms 

from home.models import HomeTasks


class HomeTasksForm(forms.ModelForm):
    
    class Meta:
        model = HomeTasks
        exclude = ('is_active','name','user',"is_deleted")
    