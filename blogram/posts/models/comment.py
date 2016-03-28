from django.db import models
from django.conf import settings

from posts.models import Post

class Comment(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )
    post = models.ForeignKey(
            "Post",
            )

    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True,)
