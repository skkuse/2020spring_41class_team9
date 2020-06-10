from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from ..model.models import Project, Developer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


def favorite(request):
    project = get_object_or_404(Project, request.POST['p_id'])
    u_id = request.session['u_id']
    developer = Developer.object.get(u_id = u_id)

    check = developer.favorite.filter(p_id = project.p_id)

    if check.exists():
        developer.favorite.remove(project)
        #project.favorite_count -= 1 
        #project.save()
        message = "favorite"
    else :
        developer.favorite.add(project)
        #project.favorite_count -= 1 
        #project.save()
        message = "cancel favorite"

    context = {
        'message' : message,
        #'num' : project.favorite_count(),
    }

    return HttpResponse(json.dumps(context), content_type= "application/json")



def follow(request):

    target = get_object_or_404(Developer, request.POST['target_id'])
    developer = get_object_or_404(Developer, u_id = request.session['u_id'])

    check = developer.follow.filter(u_id = request.POST['target_id'])

    if check.exists():
        developer.follow.remove(target)
        message ="follow"
    else :
        developer.follow.add(target)
        message = "cancel follow"

    context = {
        'message' : message,
    }

    return HttpResponse(json.dump(context), content_type="application/json")
