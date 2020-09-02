from django.urls import path
from login_interface import views

# TEMPLATE TAGGING
app_name = 'login_interface'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('login_portal/', views.login_portal, name="login_portal"),
    path('registration_portal/', views.registration_portal, name="registration_portal"),
]
