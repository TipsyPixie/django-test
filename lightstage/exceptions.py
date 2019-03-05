from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import PermissionDenied


class UserCredentialWrong(PermissionDenied):
    default_detail = _('user credential wrong')
    default_code = 'invalid_credential'


class UserInactive(PermissionDenied):
    default_detail = _('user not activated')
    default_code = 'user_inactive'


class CountryChanged(PermissionDenied):
    default_detail = _('country changed')
    default_code = 'country_changed'
