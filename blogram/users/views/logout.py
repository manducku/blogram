from django.views.generic import View 
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

class LogoutView(View):

    def get(self, request):
        logout(request)

        return redirect(
                reverse(
                    "home"
                    )
                )

