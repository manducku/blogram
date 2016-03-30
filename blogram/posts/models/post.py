from django.db import models
from django.conf import settings

from tags.models import Tag


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

    tag_set = models.ManyToManyField(
            Tag,
            blank=True,
            )

    like_user_set = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='like_post_set',
            through="Like",
            )

    def init_hash_id(self):
        from utils import get_encoded_hash_id
        self.hash_id = get_encoded_hash_id(self)
        self.save()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
                "detail",
                kwargs={
                    "slug": self.hash_id,
                    }
                )

    def __str__(self):
        return str(self.id)

    @property
    def tagified_content(self):

        tag_list = [
                word
                for word
                in self.content.split(" ")
                if word.startswith('#')
                ]

        word_list = [
                word
                for word
                in self.content.split(" ")
                ]

        tagified_word_list = []

        for word in word_list:
            if word in tag_list:
                word = "<a href='{tag_url}'>{tag_name}</a>".format(
                        tag_url=Tag.objects.get(name=word[1:]).get_absolute_url(),
                        tag_name=word,
                        )
            tagified_word_list.append(word)
            print(tagified_word_list)
        return " ".join(tagified_word_list)
