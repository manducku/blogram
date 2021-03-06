from django.conf.urls import url
from django.contrib import admin

from users.views import *
from blogram.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
]
