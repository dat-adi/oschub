# Generated by Django 3.0.3 on 2020-09-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=256)),
                ('event_start_time', models.DateTimeField()),
                ('event_details', models.TextField(max_length=500)),
                ('live_stream_link', models.URLField(blank=True, max_length=128, unique=True)),
                ('documentation_link', models.URLField(blank=True, max_length=128, unique=True)),
            ],
        ),
    ]
