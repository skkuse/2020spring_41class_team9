from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', project_list.as_view(), name = "assessment_project_list"),
    path('<int:pID>', developer_list.as_view(), name = "assessment_developer_list"),
    path('<int:pID>/<int:uID>', assessment, name= "assessment")
    ]