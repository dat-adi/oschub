from django.urls import path
from login_interface import views

# TEMPLATE TAGGING
app_name = 'login_interface'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main_page'),
    path('accounts/register/', views.registration_portal, name="registration_portal"),
]
