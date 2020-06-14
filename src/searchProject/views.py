from model.models import Project
from .forms import ProjectSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter
# Create your views here
class ProjectFilter(BaseFilter):
    search_fields ={
        'search_project' : ['name','simple_info','purpose','detailed_info'],
    }
class ProjectSearchList(SearchListView):
    model = Project
    paginate_by =9
    template_name= "searchProject/project.html"
    form_class = ProjectSearchForm
    filter_class = ProjectFilter
    ordering = '-created_time'