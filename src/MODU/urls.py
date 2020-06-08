from django.contrib import admin
from django.urls import path
import project.views

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    path('project/write/', project.views.write, name='write'),
    path('project/<int:p_id>/edit', project.views.edit, name='edit'),
    path('project/<int:p_id>/comment', project.views.comment, name='comment')
]
