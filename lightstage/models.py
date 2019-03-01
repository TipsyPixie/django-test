from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db.models import EmailField, BooleanField
from django_extensions.db.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel):
    username = EmailField(max_length=128, null=False, unique=True, db_index=True)
    is_active = BooleanField(null=False, default=False)
    is_deleted = BooleanField(null=False, default=False)
    is_blocked = BooleanField(null=False, default=False)
    is_admin = BooleanField(null=False, default=False)

    class CustomUserManager(UserManager):
        use_in_migrations = False

        def _create_user(self, username, email, password, **extra_fields):
            if not username:
                raise ValueError('The given username must be set')
            elif not password:
                raise ValueError('The given password must be set')

            username = self.model.normalize_username(username)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, username, email=None, password=None, **extra_fields):
            return self._create_user(username, email, password, **extra_fields)

        def create_superuser(self, username, email=None, password=None, **extra_fields):
            extra_fields.setdefault('is_active', True)
            extra_fields.setdefault('is_blocked', False)
            if not extra_fields.setdefault('is_admin', True):
                raise ValueError('Superuser must have is_admin=True')
            return self.create_user(username, email, password, **extra_fields)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    @classmethod
    def normalize_username(cls, username):
        return cls.objects.normalize_email(username)
