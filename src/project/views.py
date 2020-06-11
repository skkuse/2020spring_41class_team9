from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from model.models import Project, Comment, Developer
from .form import ProjectPost, CommentPost
# Create your views here.

@login_required
def write(request):
    if request.method == "POST":
        form = ProjectPost(request.POST)
        u_id = request.session['u_id']
        developer = Developer.object.get(u_id = u_id)
        if form.is_valid():
            project = form.save()
            developer.proposed_project.add(project)
            return redirect('/project/'+str(project.p_id))
    
    else:
        form = ProjectPost()
        return render(request, 'project write.html', {'form':form})

@login_required
def edit(request, projectID):
    project = get_object_or_404(Project, p_id = projectID)

    if request.method == "POST":
        form = ProjectPost(request.POST)
        if form.is_valid():
            #cleaned_data
            project.project_name = form.cleaned_data['project name']
            project.purpose = form.cleaned_data['purpose']
            project.expected_output = form.cleaned_data['output']
            project.status_choices = form.cleaned_data['status']
            project.duration_choices = form.cleaned_data['duration']
            project.simple_info = form.cleaned_data['simple info']
            project.detailed_info = form.cleaned_data['detailed info']
            # TODO
            #project.role = form.cleaned_data['role']
            #project.tag = form.cleaned_data['tag']
            
            project.save()
            return redirect('/project/'+str(project.p_id))

    else:
        form = ProjectPost(instance = project)
        return render (request, 'edit.html', {'form':form})


@login_required
def comment(request, projectID):

    if request.method == "POST":
        form = CommentPost(request.post)
        form.instance.u_id = request.session['u_id']
        form.instance.p_id = projectID
        if form.is_valid():
            comment = form.save()
    
    return redirect('/project/'+str(projectID))