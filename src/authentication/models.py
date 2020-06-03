from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class Account(AbstractBaseUser):
    class Meta:
        db_table = 'account'
        verbose_name = '계정'
        verbose_name_plural = '계정들'
        abstract = False

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = [
        'uid',
        'email',
        'is_verified',
        'name',
        'password'
    ]

    uid = models.CharField(
        primary_key=True,
        unique=True,
        max_length=128,
        verbose_name='uID'
        )

    email = models.EmailField(
        unique=True,
        verbose_name = 'email address'
        )

    is_verified = models.BooleanField(default=False, verbose_name='이메일 인증 여부') # activated when the account authenticated by email

    name = models.CharField(
        max_length=64,
        verbose_name='user name'
        )

    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    last_login = models.DateTimeField(auto_now=True, verbose_name='최근 로그인 일자')
    objects = MyUserManager()