from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from model.models import Project, Developer, Assessment
from .forms import AssessmentForm

# Create your views here.

#상호평가 버튼 클릭시
@method_decorator(login_required, name='dispatch')
class project_list(ListView):

    context_object_name = 'assessment_project_list'
    template_name = 'assessment/project_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Developer.objects.filter(uID = self.request.session.get('uID'))#.value('member_of')
        return queryset

#프로젝트 선택시
@method_decorator(login_required, name='dispatch')
class developer_list(ListView):

    context_object_name = 'assessment_developer_list'
    template_name = 'assessment/developer_list.html'

    def get_queryset(self, **kwargs):    
        project = get_object_or_404(Project, **kwargs)
        queryset = Developer.objects.all()
        queryset = queryset.filter(member_of = project)
        queryset = queryset.exclude(uID = self.request.session.get('uID'))#.valude('username') 

        return queryset


#개발자 선택시
@login_required
def assessment(request, p_id, u_id):

    subject = get_object_or_404(Developer, uID = u_id)
    auther = get_object_or_404(Developer, uID = request.session['uID'])
    project = get_object_or_404(Project, p_id = p_id)

    if request.method =="POST":
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.subject = subject
            assessment.auther = auther
            assessment.project = project
            form.save()
            return redirect('mypage/assessment/'+str(p_id))

    else:
        form = AssessmentForm()
        return render(request, 'assessment/assessment.html', {'form':form})





