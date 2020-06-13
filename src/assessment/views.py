from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from model.models import Project, Developer, Assessment, memberModel
from .forms import AssessmentForm

# Create your views here.

#상호평가 버튼 클릭시
@method_decorator(login_required, name='dispatch')
class Project_list(ListView):

    context_object_name = 'assessment_project_list'
    template_name = 'assessment/project_list.html'
    paginate_by = 10

    def get_queryset(self):

        queryset = Developer.objects.filter(uID = self.request.session.get('uID'))#.value('member_of')

        #이미 평가가 완료된 프로젝트 제외

        #유저가 작성한 평가들
        queryset2 = Assessment.object.all()
        user = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset2 = queryset2.filter(auther = user)

        result = queryset

        for member_of in queryset :
            #하나의 프로젝트에 대해 유저가 작성한 평가들
            queryset3 = queryset2.filter(project = member_of)
            #해당 프로젝트의 멤버 목록
            mem = get_object_or_404(memberModel, project = member_of)
            #작성되지 않은 평가가 있는지의 여부
            flag = 0
            for member in mem :
                if not member in queryset3.subject :
                    flag = 1
                    break 
            #해당 프로젝트에 대한 모든 평가가 작성 되었을 경우
            if flag == 0 :
                result = result.exclude(member_of = member_of)

        try:
            return result
        
        except result.DoesNotExist: 
            raise Http404("평가 가능한 프로젝트가 없습니다.")



#프로젝트 선택시
@method_decorator(login_required, name='dispatch')
class Developer_list(ListView):

    context_object_name = 'assessment_developer_list'
    template_name = 'assessment/developer_list.html'
    #allow_empty = False

    def get_queryset(self, **kwargs):    
        project = get_object_or_404(Project, pID = **kwargs)
        queryset = Developer.objects.all()
        queryset = queryset.filter(member_of = project)
        #자기 자신 제외
        queryset = queryset.exclude(uID = self.request.session.get('uID'))#.valude('username') 
        #이미 작성된 경우 제외
        queryset2 = Assessment.object.all()
        user = get_object_or_404(Developer, uID = self.request.session.get('uID'))
        queryset2 = queryset2.filter(auther = user)
        queryset2 = queryset2.filter(project = project)

        for uID in queryset2.subject:
            queryset = queryset.exclude(uID = uID)

        
        try:
            return queryset
        
        except queryset.DoesNotExist: 
            raise Http404("평가 가능한 팀원이 없습니다.")
            return redirect('mypage/assessment/')
            


#개발자 선택시
@login_required
def Assessment(request, pID, uID):

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
            return redirect('mypage/assessment/'+str(pID))

    else:
        form = AssessmentForm()
        return render(request, 'assessment/assessment.html', {'form':form})

