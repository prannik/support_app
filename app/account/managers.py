from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):
        """ Create and return user with email, password """
        if email is None:
            raise TypeError('Users must have an email address')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """ Create and return user with superadmin privileges """

        if password is None:
            raise TypeError('Superusers must have a password.')

        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return self.create_user(username, email, password, **extra_fields)

    def create_staff(self, username, email, password, **extra_fields):
        """ Create and return user with user staff privileges """
        if password is None:
            raise TypeError('Superusers must have a password.')

        extra_fields['is_staff'] = True
        return self.create_user(username, email, password, **extra_fields)
