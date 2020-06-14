from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('write', ProjectCreateView.as_view(), name='write'),
    path('<pk>/edit', ProjectUpdateView.as_view(), name='edit'),
    path('<pk>/comment', comment, name='comment')
]
