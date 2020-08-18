from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """
    Auth using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None


# from django.core.exceptions import ObjectDoesNotExist

# class EmailAuthBackend(ModelBackend):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#         except ObjectDoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             User().set_password(password)
