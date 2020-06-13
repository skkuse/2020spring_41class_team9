from django.urls import path
from searchProject.views import *

urlpatterns = [path('search', ProjectSearchList.as_view()),]