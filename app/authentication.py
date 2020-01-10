from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication, exceptions

from app import models


class ApplicationUser(object):
    @property
    def is_authenticated(self):
        return True


class ApplicationAuthentication(authentication.TokenAuthentication):
    model = models.Application

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request)
        if not auth:
            return None
        try:
            token = auth.decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return ApplicationUser(), token
