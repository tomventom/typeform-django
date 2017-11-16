from django.conf.urls import url

from accounts.views import HomeView, RegisterView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = "home"),
    url(r'^register/$', RegisterView.as_view(), name = "register"),
]
