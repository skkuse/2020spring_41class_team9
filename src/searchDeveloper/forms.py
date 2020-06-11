from django import forms

class DeveloperSearchForm(forms.Form):
    search_developer = forms.CharField(label='Search Developer')