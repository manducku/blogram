from django.db import models
from django.conf import settings


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

    def init_hash_id(self):
        from utils.hash_id import get_encoded_hash_id
        self.hash_id = get_encoded_hash_id(self)
        self.save()
