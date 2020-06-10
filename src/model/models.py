from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError

# Create your models here.

# TODO: use PREDEFINED values rather than raw digits


class Project(models.Model):
    p_id = models.AutoField(
        verbose_name = 'project ID',
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
        verbose_name = 'purpose of project',
        name = 'purpose',
        max_length = 500)

    expected_output = models.TextField(
        verbose_name = 'output',
        name = 'output',
        max_length = 500)

    STATUS_WAIT = 'wait'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETE = 'complete'

    status_choices = [(
        (STATUS_WAIT, 'waiting for your participation'),
        (STATUS_IN_PROGRESS, 'in progress'),
        (STATUS_COMPLETE, 'complete')
        )]
    
    DURATION_1MTH = '1MTH'
    DURATION_3MTH = '3MTH'
    DURATION_6MTH = '6MTH'
    DURATION_9MTH = '9MTH'
    DURATION_1YR = '1YR'
    DURATION_OVER1YR = 'OVER1YR'

    duration_choices = [(
        (DURATION_1MTH, '1 month'),
        (DURATION_3MTH, '3 months'),
        (DURATION_6MTH, '6 months'),
        (DURATION_9MTH, '9 months'),
        (DURATION_1YR, '1 year'),
        (DURATION_OVER1YR, 'over a year')
        )]

    created_time = models.DateTimeField(
        auto_now_add = True)

    last_edited_time = models.DateTimeField(
        auto_now = True)

    simple_info = models.TextField(
        verbose_name = 'project simple info',
        name = 'simple info',
        max_length = 500)

    detailed_info = models.TextField(
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
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(
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

class Developer(AbstractBaseUser):
    u_id = models.AutoField(
        verbose_name = 'user ID',
        name = 'uID',
        primary_key=True,
        unique=True)

    USERNAME_FIELD = 'u_id'

    username = models.CharField(
        verbose_name = 'user name',
        name = 'name',
        max_length = 20)

    email = models.EmailField(
        verbose_name = 'user email',
        name = 'email',
        blank = False)

    EMAIL_FIELD = 'email'

    is_active = models.BooleanField()       # is verified by an email link

    profile_image_path = models.ImageField(
        verbose_name = 'profile image of a developer',
        name = 'profile img',
        upload_to = 'uploads/user_{0}'.format(u_id),
        validators = [validate_file_size],
        # TODO: blank or null
        #       what is suitable if no uploaded img, deleted or else?
        blank = True,
        null = True)

    portfolio = models.TextField(
        verbose_name = 'portfolio text',
        name = 'portfolio',
        max_length = 5000,
        blank = True)

    proposed_projects = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'developers',
        related_query_name = 'developer')

    # TODO: use through model instead of using direct m2m model
    #       prevent self object reference
    follow = models.ManyToManyField(
        "self",
        related_name = 'developers',
        related_query_name = 'developer')

    favorite = models.ManyToManyField(
        'Project',
        related_name = 'developers',
        related_query_name = 'developer')

    member_of = models.ManyToManyField(
        'Project',
        related_name = 'developers',
        related_query_name = 'developer')

    # TODO: separate
    invite = models.ManyToManyField(
        'Project',
        related_name = 'developers',
        related_query_name = 'developer')

    class Meta:
        verbose_name = 'developer'
        ordering = ['u_ID']

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n".format(
            self.profile_image_path, 
            self.portfolio,
            self.proposed_projects,
            self.follow,
            self.favorite,
            self.invite)
    
    def validate_file_size(value):
        filesize = value.size
        if filesize > 10485760:
            raise ValidationError("The maximum file size that can be uploaded is 10MB")
        else:
            return value

class Assessment(models.Model):
    a_id = models.AutoField(
        verbose_name = 'assessment ID',
        name = 'aID',
        primary_key = True,
        unique = True)
    
    subject = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment')

    auther = models.ForeignKey(
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

    class Meta: 
        verbose_name = 'assessment'

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(
            self.subject,
            self.auther,
            self.project,
            self.score_ideation,
            self.score_development,
            self.score_communication,
            self.score_other,
            self.opinion)

    def rangeValidation(self, value):
        if not value in range(1, 6):
            raise ValidationError("not a valid value")
        else :
            return value

class Message(models.Model):
    m_id = models.AutoField(
        verbose_name = 'message ID',
        name = 'mID',
        primary_key = True,
        unique = True)

    is_read = models.BooleanField(
        verbose_name = 'is read by a receiver',
        name = 'is read')

    sent_time = models.DateTimeField(
        verbose_name = 'message sent time',
        name = 'sent time')

    text = models.TextField(
        verbose_name = 'message text',
        name = 'text')

    sender = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'messages',
        related_query_name = 'message'
        )
    
    receiver = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'messages',
        related_query_name = 'message'
        )

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return self.text

class Notification(models.Model):
    n_id = models.AutoField(
        verbose_name = 'notification ID',
        name = 'nID',
        primary_key = True,
        unique = True)

    is_read = models.BooleanField(
        verbose_name = 'is read by a receiver',
        name = 'is read')

    sent_time = models.DateTimeField(
        verbose_name = 'notification sent time',
        name = 'sent time')

    text = models.TextField(
        verbose_name = 'notification text',
        name = 'text')
    
    receiver = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'notifications',
        related_query_name = 'notification'
        )

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return self.text
