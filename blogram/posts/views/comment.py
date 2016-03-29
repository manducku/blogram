from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from posts.models import Comment, Post


@method_decorator(require_POST, name="dispatch")
class CommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = ['content']

    def form_valid(self, form):
        post = Post.objects.get(
                hash_id=self.kwargs.get('slug')
                )

        form.instance.post = post
        form.instance.user = self.request.user

        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        post = Post.objects.get(
                hash_id=self.kwargs.get('slug')
                )
        return post.get_absolute_url()
