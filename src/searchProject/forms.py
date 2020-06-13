from django import forms
from model.models import Project

class ProjectSearchForm(forms.Form):
    search_project = forms.CharField(
        required = False,
        label='')