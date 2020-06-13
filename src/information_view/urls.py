from .views import *
from django.urls import path
from information_view.views import *

urlpatterns = [
    path('project/<int:pk>', Project_detail_view.as_view()),
    path('developer/<int:pk>', Developer_detail_view.as_view()),
]