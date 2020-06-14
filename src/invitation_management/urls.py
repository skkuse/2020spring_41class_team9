from .views import *
from django.urls import path
from invitation_management.views import *

urlpatterns = [

    path('developer/invite/<int:uID>', Invite_projet_list.as_view, name='inv_projects'),     
    path('invite/<int:uID>/<int:pID>/', Invite.as_view(), name='invite'),
    
    path('mypage/invitation/' Invite_projet_list.as_view(), name='inv_list'),
    path('accept/<int:pID>/', InvitationAccept.as_view(), name='accept'),
    path('den/<int:pID>/', InvitationDeny.as_view(), name='deny'),
]