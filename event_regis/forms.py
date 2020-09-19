from django import forms
from event_regis.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_start_time', 'event_details', 'live_stream_link', 'documentation_link')

