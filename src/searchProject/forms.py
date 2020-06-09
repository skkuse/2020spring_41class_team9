from django import forms

class ProjectrSearchForm(forms.Form):
    search_project = forms.Charfield(label='Search Project')