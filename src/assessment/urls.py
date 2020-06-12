from django.contrib import admin
from django.urls import path
from assessment.views import *

urlpatterns = [
    path('', project_list),
    path('<int:p_id>', developer_list),
    path('<int:p_id>/<int:u_id>', assessment)
]
