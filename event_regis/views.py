from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView,
                                  ListView, DetailView,
                                  UpdateView, DeleteView)
from . import models


# Listing out all the events
class EventListView(LoginRequiredMixin, ListView):
    context_object_name = 'events'
    model = models.Event


# Home page for the event access
class EventHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'event_regis/event_home_page.html'


# Shows the details of the event
class EventDetailView(LoginRequiredMixin, DetailView):
    model = models.Event


# Addition of the event
class RegisterEvent(LoginRequiredMixin, CreateView):
    fields = ('event_name', 'event_start_time', 'event_details', 'live_stream_link', 'documentation_link')
    model = models.Event


# Updating the event
class EventUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = 'event_regis/event_detail.html'
    form_class = EventForm
    model = models.Event


# Deleting the event
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Event
    success_url = reverse_lazy('event_regis:list')


# TODO: Need to add in the method to send a call to the API
