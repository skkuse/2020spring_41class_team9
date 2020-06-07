from django.db import models
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError

# Create your models here.

class Project(models.Model):
    p_id = models.AutoField(
        verbose_name = 'project id'
        name = 'pID',
        primary_key = True,
        unique = True)

    project_name = models.TextField(
        verbose_name = 'project name',
        name = 'project name',
        max_length = 100)

    # TODO: REMOVE!
    #proposer_name = models.TextField(
    #    verbose_name = 'proposer name',
    #    name = 'proposer name',
    #    max_length = 20)

    purpose = models.TextField(
        verbose_name = 'purpose',
        name = 'purpose',
        max_length = 500)

    expected_output = models.TextField(
        verbose_name = 'output',
        name = 'output',
        max_length = 500)

    STATUS_WAIT                 = 'wait'
    STATUS_IN_PROGRESS          = 'in_progress'
    STATUS_COMPLETE             = 'complete'

    status_choices = [(
        (STATUS_WAIT,           'waiting for your participation'),
        (STATUS_IN_PROGRESS,    'in progress'),
        (STATUS_COMPLETE,       'complete'))]
    
    DURATION_1MTH               = '1MTH'
    DURATION_3MTH               = '3MTH'
    DURATION_6MTH               = '6MTH'
    DURATION_9MTH               = '9MTH'
    DURATION_1YR                = '1YR'
    DURATION_OVER1YR            = 'OVER1YR'

    duration_choices = [(
        (DURATION_1MTH,         '1 month'),
        (DURATION_3MTH,         '3 months'),
        (DURATION_6MTH,         '6 months'),
        (DURATION_9MTH,         '9 months'),
        (DURATION_1YR,          '1 year'),
        (DURATION_OVER1YR,      'over a year'))]

    created_time = models.DateTimeField(
        auto_now_add = True)

    last_edited_time = models.DateTimeField(
        auto_now = True)

    project_simple_info = models.TextField(
        verbose_name = 'simple info',
        name = 'simple info',
        max_length = 500)

    project_detailed_info = models.TextField(
        verbose_name = 'detailed info',
        name = 'detailed info',
        max_length = 5000)

    tag = TaggableManager()
    
    # TODO: enable role and count pairing
    role = TaggableManager()

    # TODO: REMOVE
    ##Member of-Project
    #members = models.ManyToManyField(
    #    'Developer',
    #    on_delete = models.CASCADE,
    #    related_name = 'projects',
    #    related_query_name = 'project')

    class Meta:
        verbose_name = 'project'
        ordering = ['created_time']

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
            self.last_edited_time)

class Comment(models.Model):
    c_id = models.AutoField(
        verbose_name = 'comment ID',
        name = 'comment ID',
        primary_key = True,
        unique = True)

    comment_text = models.TextField(
        verbose_name = 'comment text',
        name = 'comment text',
        max_length = 500)

    sent_time = models.DateTimeField(
        auto_now_add = True)

    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'comments',
        related_query_name = 'comment')

    writer = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'comments',
        related_query_name = 'comment')

    class Meta:
        verbose_name = 'comment'
        ordering = ['sent_time']

    def __str__(self):
        return "{}\n{}\n{}\n".format(
            self.writer,
            self.sent_time,
            self.comment_text)

class Assessment(models.Model):
    a_id = models.AutoField(
        verbose_name = 'assessment id'
        name = 'aID',
        primary_key = True,
        unique = True)
    
    subject = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment')

    writter = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment')

    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment')

    score_ideation = models.IntegerField(
        verbose_name = 'score for the ideation',
        name = 'ideation score',
        validators = [rangeValidation])

    score_development = models.IntegerField(
        verbose_name = 'score for the development',
        name = 'development score',
        validators = [rangeValidation])

    score_communication = models.IntegerField(
        verbose_name = 'score for the communication',
        name = 'communication score',
        validators = [rangeValidation])

    score_other = models.IntegerField(
        verbose_name = 'score for other parts',
        name = 'etc. score',
        validators = [rangeValidation])

    opinion = models.TextField(
        verbose_name = 'assessment opinion for overall parts',
        name = 'opinion',
        max_length = 100)

    # Metadata
    class Meta: 
        verbose_name = 'assessment'

    # Methods
    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(
            self.subject, 
            self.writter, 
            self.project, 
            self.score_ideation, 
            self.score_development, 
            self.score_communication, 
            self.score_other, 
            self.opinion)

    def rangeValidation(self, value):
        if not value in [1, 2, 3, 4, 5]:
            raise ValidationError("not a valid value")
        else :
            return value
