from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^dinner/', include('littomsit.dinner.urls')),

     #Uncomment the admin/doc line below to enable admin documentation:
     # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

     (r'^admin/', include(admin.site.urls)),
)