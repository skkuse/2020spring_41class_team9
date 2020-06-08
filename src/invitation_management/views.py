from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project, Developer, Invitation

# previous change: invitation inquiry is done through message
# so here, we only deal with (1) developer inviting other developer in a project,
# and (2) developer accepting or rejecting invitations
# Create your views here.


def invite(request, userID):
    
    developer = get_object_or_404(Developer, userID)
    u_id = request.u_id
    project = Project.object.get(u_id = u_id)
    check = Invitation.object.get(p_id = p_id)

    if check.exists():
        check.invite.remove(project)
    else:
        check.invite.add(project)

    return redirect('/developer/'+str(userID))

def invitationAccept(request, userID):
    
    invitation = get_object_or_404(Invitation, userID)
    u_id = request.u_id
    i_id = request.i_id
    check = invitation.object.get(i_id = i_id)

    # 이미 수락한거라면 초대 리스트에서 삭제
    if check.exist():
        check.is_accepted = TRUE
        return check.remove(i_id)

    else:
        # 초대 거절후 초대 리스트에서 삭제
        # accepted = FALSE
        return invitation.remove(i_id)

        # 초대 아무 반응 안할시 그대로 리턴
        
    
    return redirect('/mypage/invitation/'+str(userID))
