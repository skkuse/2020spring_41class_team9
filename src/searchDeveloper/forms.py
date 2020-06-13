from django import forms
from model.models import Developer

class DeveloperSearchForm(forms.Form):
    search_developer = forms.CharField(
        required = False,
        label='Search Developer')