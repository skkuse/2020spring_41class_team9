from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project, name='search-project'),
    path('developer/', views.developer, name='search-developer'),
]