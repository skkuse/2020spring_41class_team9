from django.conf.urls import url
from .views import *
urlpatterns = [url(r'^searchdeveloper/$', SearchDeveloperFormView.as_view(), name='searchdeveloper'),]