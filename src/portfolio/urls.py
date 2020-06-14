from django.contrib import admin
from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('developer/<pk>/edit', PortfolioUpdateView.as_view(), name='edit')
]