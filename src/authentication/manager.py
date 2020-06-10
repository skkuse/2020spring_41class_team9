import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager

User = get_user_model()

class CustomUserManager(BaseUserManager):
    def filter_email(email = None):
        return True # TODO: filter email

    def firebase_try_sign_up(email = None, password = None):
        if not email or not password:
            return None
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + FIREBASE_API_KEY
        payload = dict(email = email, password = password, returnSecureToken = "True")
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

    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)

        if not filter_email(email):
            raise ValueError(_('User need school mail address'))

        if not username:
            raise ValueError(_('Users must have an username'))
        
        if not password:
            raise ValueError(_('Users must have a password'))

        user = self.model(
            email = email,
            username = username,
            password = set_unusable_password(),
            is_active = False,
            # TODO: how to add imagefield?
            portfolio = '')

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