from django.shortcuts import render
from django.db.models import Q
from model.models import Project
from searchProject.forms import ProjectSearchForm
from django.views.generic.edit import FormView

# Create your views here
class SearchProjectFormView(FormView):
    form_class = ProjectSearchForm
    template_name='searchProject/project.html'

    def form_valid(self, form):
        search_project= self.request.GET['search_project']
        project_list=Project.objects.filter(Q(p_id__icontains=search_project)|Q(detailed_info__icontains=search_project)|Q(project_name__icontains=search_project)).order_by('created_time')
        context={}
        context['form']=form
        context['search_term']=search_project
        context['object_list']=project_list

        return render(self.request, self.teamplate_name, 
        context)
   