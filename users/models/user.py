from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_comment = models.CharField(
            max_length=100,
            blank=True,
            null=True,
            )

    class Meta:
        verbose_name = "member info"
        verbose_name_plusa = verbose_name
