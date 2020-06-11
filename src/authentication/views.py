from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

User = get_user_model()

# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/'

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = '/login.html' # TODO

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to log in.', extra_tags='danger')
        return super().form_invalid(form)