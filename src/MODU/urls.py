from django.contrib import admin
from django.urls import path
import assessment.views

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    
    #assessment
    path('mypage/assessment/<int:p_id>', assessment.views.project_select, name = 'project_select'),
    path('mypage/assessment/<int:p_id>/<int:u_id>', assessment.views.developer_select, name = 'developer_select'),
    path('mypage/assessment/<int:p_id>/<int:u_id>/write', assessment.views.developer_select, name = 'assessment_write'),
        
]
