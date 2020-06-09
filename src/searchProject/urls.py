from django.conf.urls import url
from .views import *
urlpatterns = [url(r'^searchproject/$', SearchProjectFormView.as_view(), name='searchproject'),]