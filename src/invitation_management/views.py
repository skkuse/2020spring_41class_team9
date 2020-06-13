from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from model.models import Project, Developer, Invitation

# Create your views here.

class InviteListView(ListView):
    
    context_object_name = 'invite_list'
    template_name = 'searchDeveloper/invitationlist.html'
    paginate_by = 10
    
    def get_queryset(self):
        developer = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset = Invitation.objects.filter(receiver = developer)

        return queryset.order_by('sent_time')

@login_required   
def invite_accept(request, pID, uID):

    if request.method == "POST":
        developer = get_object_or_404(Developer, uID = uID)
        project = get_object_or_404(Project, pID = pID)
        invitation = get_object_or_404(Invitation, receiver = developer)
        
        developer.member_of.add(project)
        #invitation.is_accepted = True
        #invitation.save()
        invitation.project.remove(project)

        return redirect('InviteList')
    
    else:
        return render(request, 'searchDeveloper/invitationlist.html')


@login_required
def invite_reject(request, pID, uID):

    if request.method == "POST":
        developer = get_object_or_404(Developer, uID = uID)
        project = get_object_or_404(Project, pID = pID)
        invitation = get_object_or_404(Invitation, receiver = developer)
        
        invitation.project.remove(project)
        #invitation.is_accepted = False
        #invitation.save()
        return redirect('InviteList')
    
    else:
        return render(request, 'searchDeveloper/invitationlist.html')
      
