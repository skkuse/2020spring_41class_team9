from django import forms
from model.models import Project, Comment

class ProjectPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project name',
            'purpose',
            'output',
            'simple info',
            'detailed info'
            ]
        STATUS = (
            ('W', 'waiting for your participation'),
            ('P', 'in progress'),
            ('C', 'complete')
            )
        DURATION = (
            ('1', '1 month'),
            ('3', '3 months'),
            ('6', '6 months'),
            ('9', '9 months'),
            ('12', '1 year'),
            ('13', 'over a year')
            )
        widgets = {
            'status' : forms.Select(choices=STATUS, attrs={'class': 'status_choice'}),
            'duration' : forms.Select(choices=DURATION, attrs={'class': 'duration_choice'})
        }

class CommentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]

        