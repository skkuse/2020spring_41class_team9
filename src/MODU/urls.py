from django.contrib import admin
from django.urls import path
import project.views
import favorite_follow.views

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)

    path('', include('favorite_follow.urls')),
]
