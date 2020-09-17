from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView,
                                  ListView, DetailView,
                                  UpdateView, DeleteView)
from . import models


# Create your views here.
class RegisterEvent(CreateView):
    fields = ('event_name', 'event_start_time', 'event_details', 'live_stream_link', 'documentation_link')
    model = models.Event


class EventListView(ListView):
    context_object_name = 'events'
    model = models.Event


class EventHomePage(TemplateView):
    template_name = 'event_regis/event_home_page.html'
