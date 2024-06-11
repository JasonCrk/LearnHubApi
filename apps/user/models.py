from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(
            self,
            email: str,
            first_name: str,
            last_name: str,
            password=None):
        if not email:
            raise ValueError("The email is required")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, first_name: str, last_name: str, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser):
    first_name = models.CharField(verbose_name='First name', max_length=60)
    last_name = models.CharField(verbose_name='Last name', max_length=60)
    picture_url = models.URLField(
        verbose_name='Photo URL',
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='IS ACTIVE', default=True)
    is_admin = models.BooleanField(verbose_name='IS ADMIN', default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

    @property
    def is_staff(self):
        return self.is_admin

