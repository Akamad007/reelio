from django.conf.urls import include, url,patterns
from home.api import HomeTasksResource

tasks_resource = HomeTasksResource()

urlpatterns = patterns('home.views',
    # Examples:
    url(r'^$', 'home'),   
    url(r'^api/', include(tasks_resource.urls)), 
    url(r'^create/$', 'create'),         
    url(r'^edit/(\w+)/$', 'create'), 
    url(r'^trashBox/$', 'trashBox'),
   #  url(r'^$', include('home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
)