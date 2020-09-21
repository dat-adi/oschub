from django.shortcuts import render
from django.views.generic import TemplateView


class LiveStreamView(TemplateView):
    template_name = "livestream_app/livestream_event.html"

# TODO: iframe src needs to be able to take in from event components.
