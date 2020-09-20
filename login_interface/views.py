from django.shortcuts import render
from login_interface.forms import UserForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = "login_interface/main_page.html"


class UserProfileView(TemplateView):
    template_name = "login_interface/user_profile.html"


class UserRegistrationView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('dashboard:welcome')
    template_name = 'login_interface/registration_portal.html'

