from django.db import models

#Reference: https://wayhome25.github.io/django/2017/03/20/django-ep5-model/


# Create your models here.
class Project(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    pID = models.CharField(
        primary_key=True,
        max_length=20,
    )

    project_name = models.TextField(
        verbose_name='project name',
        max_length=100,
    )

    proposer_name = models.TextField(
        verbose_name='proposer name',
        max_length=20,
    ) 

    purpose = models.TextField(
        verbose_name='purpose',
        max_length=500,
    )

    expected_output = models.TextField(
        verbose_name='output',
        max_length=500,
    )

    status_choices = (
        ('status_진행중', '진행중'), 
        ('status_진행완료', '진행완료'),

    )

    duration_choices = (
        ('duration_1개월', '1개월'),
        ('duration_3개월', '3개월'),
        ('duration_6개월', '6개월'),
        ('duration_9개월', '9개월'),
        ('duration_12개월', '12개월'),
        ('duration_12개월이상', '12개월 이상'),
    )

    created_time = models.DateTimeField(auto_now_add=True)

    last_edited_time = models.DateTimeField(auto_now=True)

    project_simple_info = models.TextField(
        verbose_name='simple info',
        max_length=500,
    )

    project_detailed_info = models.TextField(
        verbose_name='detailed info',
        max_length=5000,
    )

    tag = TaggableManager(
        verbose_name='tag',
        help_text='태그',
        through='',
    )

    """https://django-taggit.readthedocs.io/en/latest/api.html"""

    role = TaggableManager(
        verbose_name='role',
        help_text='모집 역할',
        through='',
    )

    #Project-Write for-Assessment
    assessment = models.ForeignKey(
        'Assessment',
        on_delete=models.CASCADE,
        related_name='projects',
        related_query_name='project'
    )

    #Member of-Project
    members = models.ManyToManyField(
        'Developer',
        on_delete=models.CASCADE,
        related_name='projects',
        related_query_name='project'
    )

    #Project-Have-Comment
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        related_name='developers',
        related_query_name='developer'
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