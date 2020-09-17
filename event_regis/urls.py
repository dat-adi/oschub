from django.urls import path
from . import views

app_name = "event_regis"

urlpatterns = [
    path('', views.EventHomePage.as_view(), name="event_home_page"),
    path('list/', views.EventListView.as_view(), name="list"),
    path('create/', views.RegisterEvent.as_view(), name="create"),
]
