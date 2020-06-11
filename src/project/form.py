from django import forms
from model.models import Project, Comment

class ProjectPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project name',
            'purpose',
            'output',
            #'status',
            #'duration',
            'simple info',
            'detailed info'
            #'tag',
            #'role'
            ]

class CommentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]

        