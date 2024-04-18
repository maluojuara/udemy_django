from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="User's e-mail",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleansField(
        verbose_name="Is user active?",
        default=True,
    )

    is_staff = models.BooleansField(
        verbose_name="Is user from dev team?",
        default=False,
    )

    is_superuser = models.BooleansField(
        verbose_name="Is user superuser?",
        default=False,
    )

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User",
        verbose_name_plural = "Users",
        db_table = "user"
    
    def __str__(self):
        return self.email