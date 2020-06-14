from django.contrib import admin
from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('<pk>/edit', PortfolioUpdateView.as_view(), name='edit')
]