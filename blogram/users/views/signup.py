from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        User = get_user_model()
        User.objects.create(
                username=username,
                password=password,
                )

        return redirect(
                reverse(
                    "home"
                    )
                )
