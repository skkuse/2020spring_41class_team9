from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from model.models import Project, Developer, Assessment
from assessment.forms import AssessmentForm

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
        queryset = queryset.exclude(u_id = self.request.session.get('u_id'))#.valude('username') 

        return queryset

"""
distinct('name')은?
이미 작성된 경우 제외?

        queryset2 = Assessment.object.all()
        queryset2 = queryset2.filter(auther = self.request.session['user'])
        queryset2 = queryset2.filter(project = project)

        for u_id in queryset2.subject :
            queryset = queryset.exclude(u_id = u_id)

        return queryset
가능?

그럼 모든 평가가 완료된 후 평가할 대상 이 없는 경우는?

if exist()

??
"""     
    


#개발자 선택시
def assessment(request, projectID, developerID):

# 이미 작성된 경우 error?

    if request.method =="POST":
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mypage/assessment/'+str(projectID))

    else:
        form = AssessmentForm()
        return render(request, 'assessment.html', {'form':form})





