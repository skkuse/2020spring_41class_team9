from django.contrib.auth.forms import UserCreationForm
from ..model.models import Developer

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Developer
        fields = UserCreationForm.Meta.fields + ('email',)
        # TODO