from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, is_active, **kwargs):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **kwargs):
        return self._create_user(username, email, password, False, False, False, **kwargs,)

    def create_superuser(self, username, email, password=None, **kwargs):
        return self._create_user(username, email, password, True, True, True, **kwargs)

    def cod_validation(self, usr, cod_registro):
        if self.filter(id=usr, codregistro=cod_registro).exists():
            return True
        else:
            return False
