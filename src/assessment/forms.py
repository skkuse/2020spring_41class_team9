from django import forms
from ..model.models import Assessment, Developer
from .widgets import CounterTextInput, starWidget

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        field = [
            'score_ideation',
            'score_development',
            'score_communication',
            'score_other',
            'opinion'
        ]
        widgets ={
            'score_ideation' : starWidget,
            'score_development' : starWidget,
            'score_communication' : starWidget,
            'score_other' : starWidget,
            'opinion': CounterTextInput,
        }
        

