from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('write', ProjectCreateView.as_view(), name='write'),
    path('<int:p_id>/edit', ProjectUpdateView.as_view(), name='edit'),
    path('<int:p_id>/comment', comment, name='comment')
]
