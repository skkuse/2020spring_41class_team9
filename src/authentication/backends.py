import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()

class FirebaseRESTBackend(BaseBackend):
    def firebase_try_sign_in(email = None, password = None):
        if not email or not password:
            return None
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword/accounts:signInWithPassword?key=' + FIREBASE_API_KEY
        payload = dict(email = email, password = password, returnSecureToken = "True")
        response = requests.post(URL, data = payload)
        if response.status_code != 200:
            return None
        return response.json['idToken']

    def firebase_check_email_verification(id_token):
        if id_token is None:
            return None
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=' + FIREBASE_API_KEY
        payload = dict(idToken = id_token)
        response = requests.post(URL, data = payload)
        if response.status_code != 200:
            return None
        return response.json['users'][0]['emailVerified']

    def authenticate(self, request, email = None, password = None):
        id_token = firebase_try_sign_in(email, password)
        if id_token is None:
            return None
        if not firebase_check_email_verification(id_token):
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise RuntimeError('The account exists in firebase, but not exists in django.')
        if not user.is_active:
            user.is_active = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_user_permissions(self, user_obj, obj=None):
        return set()

    def get_group_permissions(self, user_obj, obj=None):
        return set()

    def get_all_permissions(self, user_obj, obj=None):
        return {
            *self.get_user_permissions(user_obj, obj=obj),
            *self.get_group_permissions(user_obj, obj=obj),
        }

    def has_perm(self, user_obj, perm, obj=None):
        return perm in self.get_all_permissions(user_obj, obj=obj)