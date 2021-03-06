from django.db import models


class Tag(models.Model):

    name = models.CharField(
            max_length=20,
            unique=True,
            )

    create_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return "#{tag_name}".format(
                tag_name=self.name,
                )
