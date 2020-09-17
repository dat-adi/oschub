from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class RegisterEvent(TemplateView):
    template_name = 'event_regis/register_event.html'
