from django.urls import path
from searchProject.views import *

urlpatterns = [path('search', SearchProjectFormView.as_view()),]

    