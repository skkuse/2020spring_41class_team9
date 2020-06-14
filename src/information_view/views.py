from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from model.models import Project, Developer, followModel
from django.views.generic import DetailView

from django.views.generic.base import View
from django.http import HttpResponseForbidden, HttpResponseRedirect
from urllib.parse import urlparse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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



@method_decorator(login_required, name='dispatch')
class Favorite(View) :
    def get(self, request, *args, **kwargs):
        if 'pID' in kwargs:
            pID = kwargs['pID']
            project = Project.object.get(pID = pID)
            uID = request.session['uID']
            user = Developer.object.get(uID = uID)
            
            fav , flag = favoriteModel.object.get_or_create(favorite = project, developer = user)

            if not flag:
                user.favorite.remove(project)
                fav.delete()
            else:
                user.favorite.add(user)

        referer_url = request.META.get('HTTP_REFERER')
        path = urlparse(referer_url).path
        return HttpResponseRedirect(path)


@method_decorator(login_required, name='dispatch')
class Follow(View) :
    def get(self, request, *args, **kwargs):
        if 'uID' in kwargs:
            followee_ID = kwargs['uID']
            followee = get_object_or_404(Developer, uID = followee_ID)
            kk = request.user
            user = get_object_or_404(Developer, uID = kk.uID)
            
            fol , flag = followModel.objects.get_or_create(follower = user, followee = followee)

            if not flag:
                user.follow.remove(followee)
                fol.delete()
            else:
                user.follow.add(followee)

        referer_url = request.META.get('HTTP_REFERER')
        path = urlparse(referer_url).path
        return HttpResponseRedirect(path)
