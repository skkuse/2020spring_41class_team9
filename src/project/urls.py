from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('write/', write, name='write'),
    path('<int:p_id>/edit', edit, name='edit'),
    path('<int:p_id>/comment', comment, name='comment')
]
