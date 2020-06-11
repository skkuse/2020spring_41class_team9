from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from model.models import Project, Developer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

@login_required
def favorite(request):
    project = get_object_or_404(Project, request.POST['p_id'])
    u_id = request.session['u_id']
    developer = Developer.object.get(u_id = u_id)

    #check = developer.favorite.filter(p_id = project.p_id)
    fav , flag = favoriteModel.object.get_or_create(favorite = project, developer = developer)

    if not flag:
        developer.favorite.remove(project)
        fav.delete()
        message = "favorite"
    else :
        developer.favorite.add(project)
        message = "cancel favorite"

    context = {
        'message' : message,
    }

    return HttpResponse(json.dumps(context), content_type= "application/json")



def follow(request):

    target = get_object_or_404(Developer, request.POST['target_id'])
    u_id = request.session['u_id']
    developer = get_object_or_404(Developer, u_id = u_id)

    #check = developer.follow.filter(u_id = request.POST['target_id'])

    fol , flag = followModel.object.get_or_create(follower = developer, followee = target)


    if not flag:
        developer.follow.remove(target)
        fol.delete()
        message ="follow"
    else :
        developer.follow.add(target)
        message = "cancel follow"

    context = {
        'message' : message,
    }

    return HttpResponse(json.dump(context), content_type="application/json")
