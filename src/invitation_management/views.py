from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from model.models import Project, Developer, Invitation

# Create your views here.

# developer 초대 버튼 클릭시
def invite_button




class InviteListView(ListView):
    
    context_object_name = 'invite_list'
    template_name = 'searchDeveloper/invitationlist.html'
    paginate_by = 10
    
    def get_queryset(self):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Invitation.objects.filter(receiver = developer)

        return queryset.order_by('sent_time')
    
def invite_accept(request, project, uID):

    context_object_name = 'invite_list'
    template_name = 'searchDeveloper/invitationlist.html'

    def get_queryset(self, **kwargs):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Invitation.objects.filter(receiver = developer)

        #Invitation의 project를 developer의 member_of에 추가하고
        developer.member_of.add(project)

        queryset = queryset.exclude(project) #?

        return queryset.order_by('sent_time')


# 초대 거절 선택시
def invite_reject(request, project, uID):

    context_object_name = 'invite_list'
    template_name = 'searchDeveloper/invitationlist.html'

    def get_queryset(self, **kwargs):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Invitation.objects.filter(receiver = developer)

        #Invitation 제거
        queryset.is_accepted = False #?

        return queryset.order_by('sent_time')
      
