from django.shortcuts import render, get_object_or_404, redirect
from ..model.models import Project, Comment
from .form import ProjectPost, CommentPost
# Create your views here.


def write(request):
    if request.method == "POST":
        form = ProjectPost(request.POST)
        if form.is_valid():
            project = form.save(commit=False)

            project.save()
            return redirect('/project/'+str(project.p_id))
    
    else:
        form = ProjectPost()
        return render(request, 'project write.html', {'form':form})


def edit(request, projectID):
    project = get_object_or_404(Project, p_id = projectID)

    if request.method == "POST":
        form = ProjectPost(request.POST)
        if form.is_valid():
            #cleaned_data
            project.project_name = form.cleaned_data['project_name']
            project.purpose = form.cleaned_data['purpose']
            project.expected_output = form.cleaned_data['expected_output']
            project.status_choices = form.cleaned_data['status_choices']
            project.duration_choices = form.cleaned_data['duration_choices']    
            project.simple_info = form.cleaned_data['simple_info']
            project.detailed_info = form.cleaned_data['detailed_info']
            project.role = form.cleaned_data['role']
            project.tag = form.cleaned_data['tag']
            
            project.save()
            return redirect('/project/'+str(project.p_id))

    else:
        form = ProjectPost(instance = project)
        return render (request, 'edit.html', {'form':form})


def comment(request, projectID):

    if request.method == "POST":
        form = CommentPost(request.post)
        form.instance.u_id = request.u_id
        form.instance.p_id = projectID
        if form.is_valid():
            comment = form.save()
    
    return redirect('/project/'+str(projectID))