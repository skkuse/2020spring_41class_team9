from django import forms

class DeveloperSearchForm(forms.Form):
    search_developer = forms.Charfield(label='Search Developer')