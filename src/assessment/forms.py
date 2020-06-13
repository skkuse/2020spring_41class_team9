from django import forms
from model.models import Assessment, Developer
from assessment.widgets import CounterTextInput, starWidget

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'ideation_score',
            'development_score',
            'communication_score',
            'etc_score',
            'opinion'
        ]
        widgets ={
            'ideation_score' : starWidget,
            'development_score' : starWidget,
            'communication_score' : starWidget,
            'etc_score' : starWidget,
            'opinion': CounterTextInput,
        }
        

