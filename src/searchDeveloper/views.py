from model.models import Developer
from .forms import DeveloperSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter
# Create your views here
class DeveloperFilter(BaseFilter):
    search_fields ={
        'search_developer' : ['name','major','languages']
    }
class DeveloperSearchList(SearchListView):
    model = Developer
    paginate_by =10
    template_name= "searchDeveloper/developer.html"
    form_class = DeveloperSearchForm
    filter_class = DeveloperFilter
    ordering = 'uID'