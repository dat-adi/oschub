from django.urls import path
from login_interface import views

# TEMPLATE TAGGING
app_name = 'login_interface'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main_page'),
    path('user/', views.UserProfileView.as_view(), name="user_profile"),
    path('accounts/register/', views.UserRegistrationView.as_view(), name="registration_portal"),
    # Testing
    path('signup/', views.signup_view, name="signup"),
]
