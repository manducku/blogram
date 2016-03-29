from django.views.generic import DetailView

from posts.models import Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post 
    slug_field = "hash_id" 
