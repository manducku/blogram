from django.db import models
from django.conf import settings


class Follow(models.Model):
    followee = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name="+"
            )
    follower = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name="+"
            )
    create_at = models.DateTimeField(
            auto_now_add=True,
            )
    update_at = models.DateTimeField(
            auto_now=True,
            )
