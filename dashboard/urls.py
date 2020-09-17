from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.WelcomeView.as_view(), name="welcome"),
    path('registration/', views.registration, name='registration_page'),
]
