from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import auth
from .models import Project, Developer
from django.contrib.auth.decorators import login_required

@login_required
def favorite(request, projectID):
    project = get_object_or_404(Project, projectID)
    u_id = request.u_id
    developer = Developer.object.get(u_id = u_id)

    check = developer.favorite.filter(p_id = project.p_id)

    if check.exists():
        developer.favorite.remove(project)
        #project.favorite_count -= 1 
        #project.save()
    else :
        developer.favorite.add(project)
        #project.favorite_count -= 1 
        #project.save()

    return redirect('/project/'+str(projectID))

def follow(request, targetID):
    target = get_object_or_404(Developer, targetID)
    u_id = request.u_id
    developer = Developer.object.get(u_id = u_id)

    check = developer.follow.filter(u_id = target.u_id)

    if check.exists():
        developer.follow.remove(target)
    else :
        developer.follow.add(target)

    return redirect('/developer/'+str(targetID))
