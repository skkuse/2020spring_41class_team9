from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Project(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    p_id = models.AutoField(
        verbose_name='project id'
        name='project id',
        primary_key=True
    )

    project_name = models.TextField(
        verbose_name='project name',
        name='project name',
        max_length=100
    )

    proposer_name = models.TextField(
        verbose_name='proposer name',
        name='proposer name',
        max_length=20
    ) 

    purpose = models.TextField(
        verbose_name='purpose',
        name='purpose',
        max_length=500
    )

    expected_output = models.TextField(
        verbose_name='output',
        name='output',
        max_length=500
    )

    status_choices = (
        ('status_모집중', '모집중'),
        ('status_진행중', '진행중'), 
        ('status_진행완료', '진행완료')
    )

    duration_choices = (
        ('duration_1개월', '1개월'),
        ('duration_3개월', '3개월'),
        ('duration_6개월', '6개월'),
        ('duration_9개월', '9개월'),
        ('duration_12개월', '12개월'),
        ('duration_12개월이상', '12개월 이상')
    )

    created_time = models.DateTimeField(auto_now_add=True)

    last_edited_time = models.DateTimeField(auto_now=True)

    project_simple_info = models.TextField(
        verbose_name='simple info',
        name='simple info',
        max_length=500
    )

    project_detailed_info = models.TextField(
        verbose_name='detailed info',
        name='detailed info',
        max_length=5000
    )

    tag = TaggableManager()


    role = TaggableManager()

    #Member of-Project
    members = models.ManyToManyField(
        'Developer',
        on_delete=models.CASCADE,
        related_name='projects',
        related_query_name='project'
    )

    # Metadata
    class Meta:
        verbose_name = 'project'
        ordering = ['created_time']

    # Methods
    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n" .format(
            self.project_name, 
            self.proposer_name, 
            self.status_choices, 
            self.project_simple_info, 
            self.duration_choices, 
            self.expected_output,
            self.role,
            self.tag,
            self.project_detailed_info,
            self.last_edited_time )