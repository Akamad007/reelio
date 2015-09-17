from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.contrib import messages

from reelio.utils import urlencodeSerializer
from home.authentication import MyAuthentication
from home.forms import HomeTasksForm
from home.models import HomeTasks



        

class HomeTasksResource(ModelResource):
    
    class Meta:
        queryset = HomeTasks.objects.filter(is_deleted = False)
        resource_name = 'tasks'
        authorization = Authorization()
        authentication = MyAuthentication()
        excludes = [ 'datetime']
        allowed_methods = ['get','post','put','patch']
        serializer = urlencodeSerializer()
        always_return_data = True
            
    def obj_create(self, bundle, **kwargs):      
           
        taskForm = HomeTasksForm(bundle.data)                    
        if taskForm.is_valid():    
            messages.success(bundle.request,"The task is successfully added") 
            if "summary" not in bundle.data:
                bundle.data['summary'] = ""     
            returnData =  super(HomeTasksResource, self).obj_create(bundle,user = bundle.request.user)                
            return returnData 
        
    def obj_update(self, bundle, **kwargs):        
       
        taskForm = HomeTasksForm(bundle.data)                 
        returnData = None
        if taskForm.is_valid() and bundle.request.method =="PUT":             
            messages.success(bundle.request,"The task is updated successfully") 
            
            if "summary" not in bundle.data:
                bundle.data['summary'] = ""
            bundle.data['user'] = bundle.request.user
            returnData =  super(HomeTasksResource, self).obj_update(bundle,user = bundle.request.user,id=int(kwargs['pk']))            
             
        elif bundle.request.method == "PATCH":
             
            if bundle.data['is_active']:
                if bundle.data['is_active'].lower() == "false":
                    bundle.data['is_active'] = False
                    messages.success(bundle.request,"The task is trashed successfully")
                elif bundle.data['is_active'].lower() == "true":
                    bundle.data['is_active'] = True
                    messages.success(bundle.request,"The task is restored successfully")
                returnData =  super(HomeTasksResource, self).obj_update(bundle,is_active = bundle.data['is_active'] ,id=int(kwargs['pk']))                        
            elif bundle.data['is_deleted']:
                messages.success(bundle.request,"The task is deleted forever")
                returnData =  super(HomeTasksResource, self).obj_update(bundle,is_deleted = True ,id=int(kwargs['pk']))               
        return returnData 
        
   
        
          
            
     
   
        
           