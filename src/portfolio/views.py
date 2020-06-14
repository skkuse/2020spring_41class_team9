from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from model.models import Developer
from project.form import PortfolioPost
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

@method_decorator(login_required, name='dispatch')
class PortfolioUpdateView(UserPassesTestMixin,UpdateView):
    model = Developer
    fields = [  'major','portfolio','languages',]
    template_name = 'searchDeveloper/addportfolio.html'

    def test_func(self):
        developer = self.get_object()
        return self.request.user == self.object.uID

    def get_success_url(self):
        developer = self.get_object()
        return '/developer/' + str(self.object.uID)



