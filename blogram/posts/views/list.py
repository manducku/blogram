from django.views.generic import ListView

from posts.models import Post
from posts.views.base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"
