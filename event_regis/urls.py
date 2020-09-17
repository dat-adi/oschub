from django.urls import path
from . import views

app_name = "event_regis"

urlpatterns = [
    path('', views.RegisterEvent.as_view()),
]
