from django.contrib import admin
from django.urls import path
from invitation.views import *

urlpatterns = [
    path('invitation_management/', InviteListView.as_view(), name='InviteList'),

]