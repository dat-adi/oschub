from django.shortcuts import render
from django.http import HttpResponse
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
    registration_list = {
        'advice': 'Still isn\'t up.'
    }
    return render(request, 'login_interface/registration_portal.html', context=registration_list)
