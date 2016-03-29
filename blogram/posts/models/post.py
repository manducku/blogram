from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )
    image = models.ImageField()
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True,)

    hash_id = models.CharField(
            max_length=8,
            blank=True,
            null=True,
            unique=True,
            )

    def init_hash_id(self):
        from utils import get_encoded_hash_id
        self.hash_id = get_encoded_hash_id(self)
        self.save()
