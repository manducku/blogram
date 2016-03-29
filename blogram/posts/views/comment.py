from django.views.generic import CreateView

from posts.models import Comment, Post


class CommentCreateView(CreateView):

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
