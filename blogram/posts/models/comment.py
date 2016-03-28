from django.db import models
from django.conf import settings


class Comment(models.Model):

    hash_id = models.CharField(
            max_length=8,
            blank=True,
            null=True,
            unique=True,
            )

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )
    post = models.ForeignKey(
            "Post",
            )

    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True,)

    def init_hash_id(self):
        from hashids import Hashids
        hashids = Hashids(salt="manducku", min_length=4)
        return hashids.encode(self.id)
