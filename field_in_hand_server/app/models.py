# coding=utf-8
from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import User

class Point(models.Model):
    localityId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    localityName = models.CharField(max_length=100)
    dataId = models.UUIDField(default=uuid.uuid4, editable=False)
    datatype = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    x = models.DecimalField(max_digits=20, decimal_places=10)
    y = models.DecimalField(max_digits=20, decimal_places=10)
    h = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    altitude = models.DecimalField(max_digits=20, decimal_places=10)
    horiz_precision = models.DecimalField(max_digits=20, decimal_places=10)
    vert_precision = models.DecimalField(max_digits=20, decimal_places=10)
    distanceNS = models.DecimalField(max_digits=20, decimal_places=10)
    distanceEW = models.DecimalField(max_digits=20, decimal_places=10)
    planeType = models.CharField(max_length=20)
    dip = models.FloatField()
    dipAzumuth = models.FloatField()
    speed = models.FloatField()
    plunge = models.CharField(max_length=20)
    plungeAzimuth = models.CharField(max_length=20)
    strike = models.FloatField()
    declination = models.FloatField()
    unitId = models.CharField(max_length=20)
    timedate = models.DateTimeField(default=now(), editable=True)
    notes = models.TextField()
    comments = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.localityId

class AppUser(User):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    usertype = models.CharField(max_length=20)
    databaseSize = models.IntegerField()
    language = models.CharField(max_length=20)
    vectorgraphNumber = models.IntegerField()
# Create your models here.
