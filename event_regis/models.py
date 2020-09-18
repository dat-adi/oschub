from django.db import models
from django.urls import reverse


class Event(models.Model):
    event_name = models.CharField(max_length=256, unique=True)
    event_start_time = models.DateTimeField()
    event_details = models.TextField()
    live_stream_link = models.URLField(max_length=128, unique=True, blank=True)
    documentation_link = models.URLField(max_length=128, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("event_regis:detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.event_name

