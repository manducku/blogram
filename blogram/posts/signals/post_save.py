from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from tags.models import Tag


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance.init_hash_id()

    str_split = instance.content.split(" ")
    tag_list = [
            word[1:]
            for word
            in str_split
            if word.startswith('#')
            ]

    for tag_name in tag_list:
            tag, tag_is_created = Tag.objects.get_or_create(
                    name=tag_name
                    )
            instance.tag_set.add(tag)
