from django.shortcuts import render
from django.views.generic import DetailView
from event_regis import models


class LiveStreamView(DetailView):
    template_name = "livestream_app/livestream_event.html"
    model = models.Event

