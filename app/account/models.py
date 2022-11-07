from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.account.managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ General model user """

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(db_index=True, max_length=128, unique=True)
    email = models.EmailField(max_length=256, unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True, verbose_name='Is the account active')
    is_staff = models.BooleanField(default=False, verbose_name=' Is an employee account')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email} - Staff:{self.is_staff} - Active:{self.is_active}'

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.username}'

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
