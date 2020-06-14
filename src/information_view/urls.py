from .views import *
from django.urls import path
from information_view.views import *

urlpatterns = [
    path('project/<pk>', Project_detail_view.as_view()),
    path('developer/<pk>', Developer_detail_view.as_view()),
    
    path('favorite/<int:pID>/', Favorite.as_view(), name='favorite'),
    path('developer/<int:uID>/', Follow.as_view(), name='follow'),
]