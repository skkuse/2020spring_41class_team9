from django import forms
from model.models import Assessment, Developer
from .widgets import CounterTextInput, starWidget


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'ideation score',
            'development score',
            'communication score',
            'etc. score',
            'opinion'
        ]
        widgets ={
            'ideation score' : starWidget,
            'development score' : starWidget,
            'communication score' : starWidget,
            'etc. score' : starWidget,
            'opinion': CounterTextInput,
        }
        

