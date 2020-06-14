from django import forms
from model.models import Developer

class PortfolioPost(forms.ModelForm):
    class Meta:
        model = Developer
        fields = [
            'major',
            'portfolio',
            'languages'
            ]
      


        