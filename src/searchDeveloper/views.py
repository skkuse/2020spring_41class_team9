from django.shortcuts import render
from django.db.models import Q
from .models import Developer
from .forms import DeveloperSearchForm
from django.views.generic.edit import FormView

# Create your views here
class SearchDeveloperFormView(FormView):
    form_class = DeveloperSearchForm
    #template_name='개발자 검색 페이지'

    def form_valid(self, form):
        search_developer= self.request.DEVELOPER['search_developer']
        developer_list=Developer.objects.filter(Q(u_id__icontains=search_developer))
        context={}
        context['form']=form
        context['search_term']=search_developer
        context['object_list']=developer_list

        return render(self.request, self.#teamplate_name, 
        context)
   