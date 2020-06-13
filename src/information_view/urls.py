from .views import *
from django.urls import path

urlpatterns = [
    path('projectinfo', ProjectDetailView.as_view()),
    path('developerinfo', DeveloperDetailView.as_view()),
]