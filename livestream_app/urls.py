from django.urls import re_path
from . import views

app_name = "livestream_app"

urlpatterns = [
    re_path(r"^(?P<pk>\d+)/$", views.LiveStreamView.as_view(), name="livestream_view"),
]
