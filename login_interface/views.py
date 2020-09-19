from django.shortcuts import render
from login_interface.forms import UserForm
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)


class IndexView(TemplateView):
    template_name = 'login_interface/index.html'


def index(request):
    index_list = {
        'advice': 'Still being set up though.',
    }
    return render(request, 'login_interface/main_page.html', context=index_list)


def login_portal(request):
    login_list = {
        'advice': 'Login with your university email for easier verification',
    }
    return render(request, 'login_interface/login_portal.html', context=login_list)


def registration_portal(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'login_interface/registration_portal.html', context={'registered': registered,
                                                                                'user_form': user_form})


