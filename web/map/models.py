from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=30)
    filename = models.CharField(max_length=512)


class Coordinate(models.Model):
    lon = models.FloatField(_('Longitude'), blank=True, null=True)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    label = models.CharField(max_length=30)
    track_id = models.ForeignKey(Track)
