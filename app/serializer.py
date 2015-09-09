__author__ = 'kdq'
from app.models import AppUser, Data, Locality, Unit
from rest_framework import serializers

class AppUserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()
    class Meta:
        model = AppUser
        fields = ('uuid', 'username', 'password', 'usertype', 'databaseSize', 'language', 'vectorgraphNumber')

    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('dataId', 'datatype', 'name', 'x', 'y', 'h', 'latitude', 'longitude', 'altitude', 'horiz_precision',
                  'vert_precision', 'distanceNS', 'distanceEW', 'planeType', 'dip', 'dipAzimuth', 'speed',
                  'plunge', 'plungeAzimuth', 'strike', 'declination', 'timedate', 'notes', 'comments', 'description',
                  'heading', 'image_name', 'locality', 'unit')