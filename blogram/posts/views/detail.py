from django.views.generic import DetailView

from posts.models import Post
from posts.views.base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
    slug_field = "hash_id"
