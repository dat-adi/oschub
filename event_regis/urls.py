from django.urls import path, re_path
from . import views

app_name = "event_regis"

urlpatterns = [
    path('', views.EventHomeView.as_view(), name="event_home_page"),
    path('list/', views.EventListView.as_view(), name="list"),
    path('create/', views.RegisterEvent.as_view(), name="create"),
    re_path(r'^event/(?P<pk>\d+)$', views.EventDetailView.as_view(), name="detail"),
]
