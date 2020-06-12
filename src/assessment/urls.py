from django.contrib import admin
from django.urls import path
from .views import *

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    path("/", project_list, name ="project_list" ),
    path("/<int:p_id>", developer_list, name ="developer_list" ),
    path("/<int:p_id>/<int:u_id>", assessment, name ="assessment" ),
]
