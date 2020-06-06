from django import forms
from .models import Project

class ProjectPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'purpose', 'expected_output', 'status_choices', 'duration_choices', 'project_detailed_info', 'tag', 'role', 'members']
        