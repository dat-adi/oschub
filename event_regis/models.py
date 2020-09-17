from django.db import models


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=256)
    event_start_time = models.DateTimeField()
    event_details = models.TextField(max_length=500)
    live_stream_link = models.URLField(max_length=128, unique=True, blank=True)
    documentation_link = models.URLField(max_length=128, unique=True, blank=True)

    def __str__(self):
        return self.event_name
