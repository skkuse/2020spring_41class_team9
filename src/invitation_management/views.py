from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project, Developer, Invitation, Notification
from django.http import HttpResponse

from django.views.generic.base import View
from django.views.generic import ListView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from urllib.parse import urlparse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# previous change: invitation inquiry is done through message
# so here, we only deal with (1) developer inviting other developer in a project,
# and (2) developer accepting or rejecting invitations
# Create your views here.





# 초대 버튼 클릭시  프로젝트 목록 보여주기
class Invite_projet_list(ListView):

    context_object_name = "projects"
    template_name = "invitation_management/projects.html"

#    fiels =['participating_projects']

    def get_queryset(self):
        user = self.request.user
        #유저의 member_of 필드 참조?
        return user








# 프로젝트 목록에서 초대 버튼 클릭시
@mothod_decorator(login_required, name='dispatch')
class Invite(View):
    def get(self, request, *arg, **kwargs):
        if 'uID' in kwargs and 'pID' in kwargs:
            uID = kwargs['uID']
            subject = get_object_or_404(Developer, uID = uID)
            pID = kwargs['pID']
            project = get_object_or_404(Project, pID = pID)
            user = request.user
            message = user.name + "님께서 " + subject.name + "님을 " + project.name +"에 초대하셨습니다."

            inv , flag = Invitation.objects.get_or_create(receiver = subject, project = project)

            if not flag:
                #이미 초대 했다면 


            else if subject in project.member_of.objects.all() :
                #대상이 이미 프로젝트의 멤버라면


            else:
                inv.text = message
                inv.sent_time = timezone.datetime.now()
                inv.save()

                noti = Notification(is_read = False, sent_time = inv.sent_time, text = message, receiver = subject)
                noti.save()

                subject.invite.add(project)

            return_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)




# 초대받은 목록

class Invite_projet_list(ListView):

    context_object_name = "projects"
    template_name = "invitation_management/projects.html"
#    fiels =['projects_invited_to']

    def get_queryset(self):
        user = self.request.user
        
        #유저의 invite 필드 참조?
        return user








#초대 승낙
@mothod_decorator(login_required, name='dispatch')
class InvitationAccept(View):
    def get(self, request, *arg, **kwargs):
        if 'pID' in kwargs:
            pID = kwargs['pID']
            project = get_object_or_404(Project, pID = pID)
            user = request.user
            inviation = get_object_or_404(Invitation, receiver = user, project = project)
            #프로젝트에 멤버 등록
            project.member_of.add(user)
            #Invitation 에 승낙으로 수정
            invitation.is_accepted = True
            invitation.save()
            #초대 받은 목록에서 제거
            user.invite.remove(project)

            return_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


#초대 거부
@mothod_decorator(login_required, name='dispatch')
class InvitationDeny(View):
    def get(self, request, *arg, **kwargs):
        if 'pID' in kwargs:
            pID = kwargs['pID']
            project = get_object_or_404(Project, pID = pID)
            user = request.user
            inviation = get_object_or_404(Invitation, receiver = user, project = project)
            #프로젝트에 멤버 등록
            #project.member_of.add(user)
            #Invitation 에 승낙으로 수정
            invitation.is_accepted = False
            invitation.save()
            #초대 받은 목록에서 제거
            user.invite.remove(project)

            return_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)
