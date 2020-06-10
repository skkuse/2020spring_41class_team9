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
    path('mypage/assessment/', assessment.views.project_list.as_view(), name = 'project_list'),
    path('mypage/assessment/<int:p_id>', assessment.views.developer_list.as_view(), name = 'developer_list'),
    path('mypage/assessment/<int:p_id>/<int:u_id>', assessment.views.assessment, name = 'assessment')

]
