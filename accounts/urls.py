from django.conf.urls import url
from accounts.views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name = "register"),
]
