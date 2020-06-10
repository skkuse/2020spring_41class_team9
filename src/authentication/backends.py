import requests
from django.contrib.auth.backends import BaseBackend

class FirebaseRESTBackend(BaseBackend):
    def authenticate(self, request, email = None, password = None, **kwargs):
        if not email or not password:
            return None
        URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword/accounts:signInWithPassword?key=' + FIREBASE_API_KEY
        payload = dict(email = email, password = password, returnSecureToken = "True")
        response = requests.post(URL, data = payload)
        if response.status_code != 200:
            return None

        return None

    def get_user(self, user_id):
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