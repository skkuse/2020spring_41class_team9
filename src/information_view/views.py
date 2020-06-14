from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from model.models import Project, Developer
from django.views.generic import DetailView


# Create your views here.

# Is log in required?


class Project_detail_view(DetailView):
    model = Project
    fields = ['name', 'purpose', 'output', 'status', 'duration', 'simple_info', 'detailed_info',]
    template_name = "information_view/projectinfo.html"
    context_object_name = "project"



class Developer_detail_view(DetailView):
    model = Developer
    fields = ['name', 'email','major', 'languages', 'portfolio', 'projects_invited_to',]
    template_name = "information_view/developerinfo.html"
    context_object_name = "developer"

