from django.views.generic import View
from django.shortcuts import redirect
from posts.models import Post
from tags.models import Tag


class TagCreateView(View):
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(
                hash_id=self.kwargs.get('slug')
                )

        tag, tag_is_created = Tag.objects.get_or_create(
                name=request.POST.get('name')
                )

        post.tag_set.add(tag)

        return redirect(
                post
                )
