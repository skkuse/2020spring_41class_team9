from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, get_user_model

User = get_user_model()

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')

        # TODO