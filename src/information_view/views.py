from django.shortcuts import render, get_object_or_404
from .models import Project, Developer
from django.views import View


# Create your views here.

# Is log in required?


def project_detail_view(request, primary_key):
    project = get_object_or_404(Project, pk=primary_key)
    return render(request, 'project/project_detail.html', context={'project': project})

def developer_detail_view(request, primary_key):
    developer = get_object_or_404(Developer, pk=primary_key)
    return render(request, 'developer/project_detail.html', context={'developer': developer})


