from django.urls import path, include
from login_interface import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('login_portal/', views.login_portal, name="login_portal"),
    path('registration_portal/', views.registration_portal, name="registration_portal"),
]
