from django.urls import path
from .views import *

urlpatterns = [path('searchproject', SearchProjectFormView.as_view()),]

    