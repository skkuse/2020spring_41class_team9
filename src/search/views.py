from django.shortcuts import render

posts=[
    {
        'project_name': '소상공인 마케팅',
        'purpose': '소상공인들이 자유롭게 온라인으로 제품 판매',
        'proposer_name':'김모두',
        #'expected_ouput':'소상공인 제품 판매',
        'status_choices':'진행중',
        'duration_choices':'3개월',
        'project_simple_info':'소상공인들을 위한 플렛폼',
        'created_time': '2020-06-09'
        #'project_detailed_info':'....'
    },
    {
        'project_name': '소상공인 마케팅2',
        'purpose': '소상공인들이 자유롭게 온라인으로 제품 판매2',
        'proposer_name':'김모두2',
        #'expected_ouput':'소상공인 제품 판매',
        'status_choices':'진행중2',
        'duration_choices':'3개월2',
        'project_simple_info':'소상공인들을 위한 플렛폼2',
        'created_time': '2020-06-10'
        #'project_detailed_info':'....'
    },
    {
        'project_name': '소상공인 마케팅3',
        'purpose': '소상공인들이 자유롭게 온라인으로 제품 판매3',
        'proposer_name':'김모두3',
        #'expected_ouput':'소상공인 제품 판매',
        'status_choices':'진행중3',
        'duration_choices':'3개월3',
        'project_simple_info':'소상공인들을 위한 플렛폼3',
        'created_time': '2020-06-1'
        #'project_detailed_info':'....'
    }
]
def project(request):
    context={
        'posts': posts
    }
    return render(request, 'search/project.html',context)


def developer(request):
    return render(request, 'search/developer.html',{'title':'Developer Search'})
