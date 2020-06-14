from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from model.models import Notification

User = get_user_model()

# Create your views here.

def mainpage(request):
    return render(request, 'authentication/mainpage.html')

def verifyemail(request):
    return render(request, 'authentication/verifyemail.html')

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/verifyemail'
    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to log in.', extra_tags='danger')
        return super().form_invalid(form)

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to log in.', extra_tags='danger')
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    pass

@method_decorator(login_required, name='dispatch')
class NotificationListView(ListView):
    model=Notification
    ordering='nID'
    paginate_by=20
    template_name = 'authentication/notification.html'
