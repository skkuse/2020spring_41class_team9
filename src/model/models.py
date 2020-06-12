import random
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError
import settings
from django.contrib.auth.models import BaseUserManager

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

    purpose = models.TextField(
        verbose_name = 'purpose of project',
        name = 'purpose',
        max_length = 500)

    expected_output = models.TextField(
        verbose_name = 'output',
        name = 'output',
        max_length = 500)

    STATUS_WAIT = 'W'
    STATUS_IN_PROGRESS = 'P'
    STATUS_COMPLETE = 'C'

    status_choices = [
        (STATUS_WAIT, 'waiting for your participation'),
        (STATUS_IN_PROGRESS, 'in progress'),
        (STATUS_COMPLETE, 'complete')
        ]

    status = models.CharField(
        name = 'status',
        choices=status_choices,
        max_length=1)

    DURATION_1MTH = '1'
    DURATION_3MTH = '3'
    DURATION_6MTH = '6'
    DURATION_9MTH = '9'
    DURATION_1YR = '12'
    DURATION_OVER1YR = '13'

    duration_choices = [
        (DURATION_1MTH, '1 month'),
        (DURATION_3MTH, '3 months'),
        (DURATION_6MTH, '6 months'),
        (DURATION_9MTH, '9 months'),
        (DURATION_1YR, '1 year'),
        (DURATION_OVER1YR, 'over a year')
        ]

    duration = models.CharField(
        name = 'duration',
        choices=duration_choices,
        max_length=2)

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

    #tag = TaggableManager()
    
    # TODO: enable role and count pairing
    #role = TaggableManager()

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

    ##수정
    project = models.ForeignKey(
       'Project',
       on_delete = models.CASCADE,
       related_name = 'comments',
       related_query_name = 'comment')
    
    ##수정
    author = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'comments',
        related_query_name = 'comment')

    class Meta:
        verbose_name = 'comment'
        ordering = ['sent_time']

    def __str__(self):
        return "{}\n{}\n{}\n".format(
            self.author,
            self.sent_time,
            self.comment_text)

class CustomUserManager(BaseUserManager):
    def filter_email(email = None):
        return True # TODO: filter email

    def firebase_try_sign_up(email = None, password = None):
        if not email or not password:
            return None
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + FIREBASE_API_KEY
        payload = dict(email = email, password = password, returnSecureToken = True)
        response = requests.post(URL, data = payload)
        if response.status_code != 200:
            return None
        return response.json()['idToken']
    
    def firebase_send_email_verification(id_token):
        if id_token is None:
            return False
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=' + FIREBASE_API_KEY
        payload = dict({"X-Firebase-Locale" : 'ko-kr'})
        response = requests.post(URL, data = payload)
        if response.status_code != 200:
            return False
        return True

    def create_user(self, email, username, is_active, password = None):
        print('create_user called')
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)

        if not filter_email(email):
            raise ValueError(_('User need school mail address'))

        if not username:
            raise ValueError(_('Users must have an username'))
        
        if not password:
            raise ValueError(_('Users must have a password'))
        
        print('test')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = set_unusable_password(),
            is_active = False,
            # TODO: how to add imagefield?
            portfolio = '')

        print('test')

        id_token = firebase_try_sign_up(email, password)
        if id_token is not None:
            try:
                user = User.objects.get(email=email)
                if user.is_active:
                    return None
                else:
                    firebase_send_email_verification(id_token)
                    return user
            except User.DoesNotExist:
                raise RuntimeError('The account exists in firebase, but not exists in django.')
        else:
            user.save(using=self._db)
            return user

    def create_superuser(username_field, password=None, **other_fields):
        return None

class Developer(AbstractBaseUser):
    objects = CustomUserManager()

    u_id = models.AutoField(
        verbose_name = 'user ID',
        name = 'uID',
        primary_key=True,
        unique=True)

    USERNAME_FIELD = 'uID'

    username = models.CharField(
        verbose_name = 'user name',
        name = 'name',
        max_length = 20)

    email = models.EmailField(
        verbose_name = 'user email',
        name = 'email',
        unique=True,
        blank = False)

    EMAIL_FIELD = 'email'

    is_active = models.BooleanField(
        verbose_name = 'verified with email',
        name = 'is verified')

    def validate_file_size(value):
        filesize = value.size
        if filesize > 10485760:
            raise ValidationError("The maximum file size that can be uploaded is 10MB")
        else:
            return value

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
        related_name = 'proposed_projects',
        related_query_name = 'proposed_project')

    invite = models.ManyToManyField(
        'Project',
        related_name = 'projects_invited_to',
        related_query_name = 'project_invited_to',
        through = 'Invitation'
        )

    follow = models.ManyToManyField(
        "self",
        related_name = 'followers',
        related_query_name = 'follower',
        through = 'followModel')

    favorite = models.ManyToManyField(
        'Project',
        related_name = 'favorite_projects',
        related_query_name = 'favorite_project',
        through = 'favoriteModel')

    member_of = models.ManyToManyField(
        'Project',
        related_name = 'participating_projects',
        related_query_name = 'participating_project',
        through = 'memberModel')

    class Meta:
        verbose_name = 'developer'
        ordering = ['uID']

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n".format(
            self.profile_image_path, 
            self.portfolio,
            self.proposed_projects,
            self.follow,
            self.favorite)

class Assessment(models.Model):
    a_id = models.AutoField(
        verbose_name = 'assessment ID',
        name = 'aID',
        primary_key = True,
        unique = True)
    
    subject = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments_written_for',
        related_query_name = 'assessment')

    auther = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'assessments_written_by',
        related_query_name = 'assessment')

    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'assessments',
        related_query_name = 'assessment')

    def rangeValidation(self, value):
        if not value in range(1, 6):
            raise ValidationError("not a valid value")
        else :
            return value

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
        related_name = 'sended_messages',
        related_query_name = 'sended_message'
        )
    
    receiver = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        related_name = 'received_messages',
        related_query_name = 'received_message'
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

class Invitation(models.Model):

    i_id = models.AutoField(
        verbose_name = 'invitation ID',
        name = 'iID',
        primary_key = True,
        unique = True)

    receiver = models.ForeignKey(
        'Developer',
        on_delete = models.CASCADE,
        verbose_name = 'invited developer',
        name = 'receiver')

    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        verbose_name = 'invited project',
        name = 'project')

    is_accepted = models.BooleanField(
        verbose_name = 'is accepted by a receiver',
        name = 'is accepted')
    
    sent_time = models.DateTimeField(
        verbose_name = 'invitation sent time',
        name = 'sent time')

    text = models.TextField(
        verbose_name = 'invitation text',
        name = 'text')

    class Meta:
        unique_together = ('receiver', 'project')
    ###추가
    #    constraints = [
    #        models.CheckConstraint(
    #            check = models.Q(project__iexact = Invitation.objects.select_related('receiver').get(i_id=models.F('i_id')).values('member_of')),
    #            name="invite_projects_only_not_in_memberModel"),
    #       ]

    def __str__(self):
        return self.text

class followModel(models.Model):
    
    follower = models.ForeignKey(
        Developer,
        on_delete = models.CASCADE,
        name = 'follower',
        related_name = 'followers')
    
    followee = models.ForeignKey(
        Developer,
        on_delete = models.CASCADE,
        name = 'followee',
        related_name = 'followees')

    class Meta:
        unique_together = ('follower', 'followee')


class favoriteModel(models.Model):
    
    developer = models.ForeignKey(
        Developer,
        on_delete = models.CASCADE,)

    favorite = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,)

    class Meta:
        unique_together = ('developer','favorite')

class memberModel(models.Model):
    
    member = models.ForeignKey(
        Developer,
        on_delete = models.CASCADE,)

    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,)

    class Meta:
        unique_together = ('member','project')
