from django.contrib import admin
from ..model.models import Project, Developer, Assessment
from .forms import AssessmentForm

admin.site.register(Project)
admin.site.register(Developer)

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    form = AssessmentForm

# Register your models here.
