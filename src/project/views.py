from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectPost
# Create your views here.


def write(request):
    if request.method == "POST":
        form = ProjectPost(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.proposer_name = request.session.POST('name')
            project.save()
            return redirect('/project/'+str(project.pID))
    
    else:
        form = ProjectPost()
        return render(request, 'project write.html', {'form':form})


def edit(request, projectID):
    project = Project.objects.get(pID = projectID)

    if request.method == "POST":
        form = ProjectPost(request.POST)
        if form.is_valid():
            #cleaned_data
            project.project_name = form.cleaned_data['project name']
            project.purpose = form.cleaned_data['purpose']
            project.status_choices = form.cleaned_data['status_choices']
            project.project_simple_info = form.cleaned_data['project simple info']
            project.duration_choices = form.cleaned_data['duration_choices']    
            project.expected_output = form.cleaned_data['expected output']
            project.role = form.cleaned_data['role']
            project.tag = form.cleaned_data['tag']
            project.member = form.cleaned_data['member']
            
            project.save()
            return redirect('/project/'+str(project.pID))

    else:
        form = ProjectPost(instance = project)
        context={
            'form' : form,
            'writing' : True,
            'now' : 'edit'
        }
        return render (request, 'edit.html', context)


