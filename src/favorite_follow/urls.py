from django.contrib import admin
from django.urls import path
from .views import *

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    path('project/favorite', favorite, name='favorite'),
    path('developer/follow', follow, name='follow'),
    
]