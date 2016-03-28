from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


class LoginView(TemplateView):
    template_name = "users/login.html"

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
                username=username,
                password=password,
                )
        if user:
            login(request, user)

            return redirect(
                    reverse(
                        "home"
                        )
                    )
        else:

            return redirect(
                    reverse(
                        "login"
                        )
                    )
