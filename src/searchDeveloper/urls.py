from django.urls import path
from searchDeveloper.views import *

urlpatterns = [path('search', DeveloperSearchList.as_view()),]