from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from ..model.models import Project, Developer, Assessment
from .forms import AssessmentForm

# Create your views here.

#상호평가 버튼 클릭시
def project_list(ListView):

    context_object_name = 'assessment_project_list'
    template_name = 'assessment/project_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Developer.objects.filter(u_id = self.request.session.get('u_id'))#.value('member_of')
        return queryset

#프로젝트 선택시
def developer_list(request, projectID):

    context_object_name = 'assessment_developer_list'
    template_name = 'assessment/developer_list.html'
    project = get_object_or_404(Project, p_id = projectID)

    def get_queryset(self):
        queryset = Developer.objects.all()
        queryset = queryset.filter(member_of = project)
        queryset = queryset.exclude(u_id = self.request.session.get('u_id'))#.valude('name') 
        #developer model에 name 필드 추가?

        return queryset
    


#개발자 선택시
def assessment(request, projectID, developerID):
    if request.method =="POST":
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mypage/assessment/'+str(projectID))

    else:
        form = AssessmentForm()
        return render(request, 'assessment.html', {'form':form})


