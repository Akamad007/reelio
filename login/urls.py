from django.conf.urls import include, url,patterns
from login.api import UserResource

user_resource = UserResource()

urlpatterns = patterns('login.views',
    # Examples:
    url(r'^$', 'login'),  
    url(r'^api/', include(user_resource.urls)), 
    url(r'^signup/$', 'signup'),      
   #  url(r'^$', include('home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
)