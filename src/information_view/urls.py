from .views import *
from django.urls import path

urlpatterns = [
    path('projectinfo', project_detail_view.as_view()),
    path('developerinfo', developer_detail_view.as_view()),
]