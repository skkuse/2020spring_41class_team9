from django import forms

class ProjectSearchForm(forms.Form):
    search_project = forms.CharField(label='Search Project')