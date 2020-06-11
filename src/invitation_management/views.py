from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project, Developer, Invitation
from django.http import HttpResponse
import json

# previous change: invitation inquiry is done through message
# so here, we only deal with (1) developer inviting other developer in a project,
# and (2) developer accepting or rejecting invitations
# Create your views here.


def invite(request, userID):
    
    subject = get_object_or_404(Developer, request.POST[userID])
    developer = get_object_or_404(Developer, u_id = request.session['u_id'])
    
    check = developer.invite.filter(u_id = request.POST[userID])

    if check.exists():
        developer.invite.remove(subject)
        message = "invite"

    else :
        developer.invite.add(subject)
        message = "cancel invite"

    context = {
        'message' : message,    
    }

def invitationAccept(request, userID):
    
    invitation = get_object_or_404(Invitation, request.POST['i_id'])
    i_id = request
    u_id = request.session['u_id']

    check = invitation.object.filter(i_id = i_id)

    # Accept
    if check.exists():
        check.is_accepted = TRUE
        return check.remove(i_id)
    # Reject
    else:
        check.is_accepted = FALSE
        return
    
    return redirect('/mypage/invitation/'+str(userID))
