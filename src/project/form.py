from django import forms
from .models import Project, Comment

class ProjectPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'purpose',
            'expected_output',
            'status_choices',
            'duration_choices',
            'simple_info',
            'detailed_info',
            'tag',
            'role'
            ]

class CommentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]

        