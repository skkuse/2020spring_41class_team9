from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project, Developer, Comment
from django.views import DetailView

# Create your views here.

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'information_view/projectinfo.html'
    context_object_name = 'projectinfo'

    def get_queryset(self):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Comment.objects.filter(author = developer)

        return queryset.order_by('sent_time')


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'information_view/developerinfo.html'
    context_object_name = 'developerinfo'

    def get_queryset(self):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Comment.objects.filter(author = developer)

        return queryset.order_by('sent_time')

