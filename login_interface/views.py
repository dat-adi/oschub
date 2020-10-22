from django.shortcuts import render, redirect
from login_interface.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = "login_interface/main_page.html"


class UserProfileView(TemplateView):
    template_name = "login_interface/user_profile.html"


class UserRegistrationView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard:welcome")
    template_name = "login_interface/registration_portal.html"


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.university_id = form.cleaned_data.get("university_id")
        user.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("login_interface:main_page")
    else:
        form = SignUpForm()
    return render(request, "login_interface/signup.html", {"form": form})
