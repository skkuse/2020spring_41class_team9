from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', project_list.as_view(), name = "assessment_project_list"),
    path('<int:p_id>', developer_list.as_view(), name = "assessment_developer_list"),
    path('<int:p_id>/<int:u_id>', assessment, name= "assessment")
    ]