from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView
from model.models import Project, Comment, Developer
from project.form import ProjectPost, CommentPost
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'purpose', 'output', 'status', 'duration', 'simple_info', 'detailed_info',]
    template_name = 'searchProject/addproject.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        u_id = self.request.user.uID
        developer = Developer.objects.get(uID = u_id)
        self.object.proposer = developer
        self.object.save()
        developer.member_of.add(self.object)
        return redirect('/project/' + str(self.object.pID))

@login_required
def comment(request, projectID):

    if request.method == "POST":
        form = CommentPost(request.post)
        form.instance.u_id = request.session['u_id']
        form.instance.p_id = projectID
        if form.is_valid():
            comment = form.save()
    
    return redirect('/project/'+str(projectID))

class ProjectUpdateView(UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['name', 'purpose', 'output', 'status', 'duration', 'simple_info', 'detailed_info',]
    template_name = 'searchProject/addproject.html'

    #def form_valid(self, form):
    #    u_id = self.request.user.uID
    #    developer = Developer.objects.get(uID = u_id)
    #    self.object.proposer = developer
    #    self.object.save()
    #    developer.member_of.add(self.object)
    #    return redirect('/project/' + str(self.object.pID))

    def test_func(self):
        proj = self.get_object()
        return self.request.user == proj.proposer

    
    