from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from model.models import Project, Developer
from django.views.generic import DetailView


# Create your views here.

# Is log in required?


class Project_detail_view(DetailView):
    model = Project
    template_name = "projectinfo"
    context_object_name = "project_info"



class Developer_detail_view(DetailView):
    model = Developer
    template_name = "developerinfo"
    context_object_name = "developer_info"

