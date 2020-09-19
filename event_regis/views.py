from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EventForm
from django.views.generic import (TemplateView, CreateView,
                                  ListView, DetailView,
                                  UpdateView, DeleteView)
from . import models


# Listing out all the events
class EventListView(ListView):
    context_object_name = 'events'
    model = models.Event


# Home page for the event access
class EventHomeView(TemplateView):
    template_name = 'event_regis/event_home_page.html'


# Shows the details of the event
class EventDetailView(DetailView):
    model = models.Event


# Addition of the event
class RegisterEvent(CreateView):
    fields = ('event_name', 'event_start_time', 'event_details', 'live_stream_link', 'documentation_link')
    model = models.Event


# Updating the event
class EventUpdateView(UpdateView):
    redirect_field_name = 'event_regis/event_detail.html'
    form_class = EventForm
    model = models.Event


# Deleting the event
class EventDeleteView(DeleteView):
    model = models.Event
    success_url = reverse_lazy('event_regis:list')
