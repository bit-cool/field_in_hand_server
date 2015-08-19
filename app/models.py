# coding=utf-8
from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import User


class Data(models.Model):
    dataId = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    datatype = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    x = models.DecimalField(max_digits=20, decimal_places=10)
    y = models.DecimalField(max_digits=20, decimal_places=10)
    h = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='纬度')
    longitude = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='经度')
    altitude = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='高程')
    horiz_precision = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='水平精确度')
    vert_precision = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='垂直精确度')
    distanceNS = models.DecimalField(max_digits=20, decimal_places=10)
    distanceEW = models.DecimalField(max_digits=20, decimal_places=10)
    planeType = models.CharField(max_length=20)
    dip = models.FloatField(verbose_name='倾角')
    dipAzimuth = models.FloatField(verbose_name='倾向')
    speed = models.FloatField(verbose_name='速度')
    plunge = models.CharField(max_length=20)
    plungeAzimuth = models.CharField(max_length=20)
    strike = models.FloatField(verbose_name='走向')
    declination = models.FloatField(verbose_name='磁偏角')
    timedate = models.DateTimeField()
    notes = models.TextField(verbose_name='笔记')
    comments = models.TextField(verbose_name='评论')
    description = models.TextField(verbose_name='描述')
    heading = models.CharField(max_length=20, blank=True)
    image_name = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return str(self.localityId)


class Locality(models.Model):
    localityId = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    localityName = models.CharField(max_length=100)
    data = models.ForeignKey(Data, related_name='locality')

    def __unicode__(self):
        return self.localityName


class Unit(models.Model):
    unitId = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    unit = models.CharField(max_length=50)
    data = models.ForeignKey(Data, related_name='unit')

    def __unicode__(self):
        return self.unit


class AppUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.OneToOneField(User)
    usertype = models.CharField(max_length=20, blank=True)
    databaseSize = models.IntegerField(default=0)
    language = models.CharField(max_length=20, blank=True)
    vectorgraphNumber = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.uuid)
