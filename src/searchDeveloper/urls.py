from django.urls import path
from searchDeveloper.views import *

urlpatterns = [path('search', SearchDeveloperFormView.as_view()),]