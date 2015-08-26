__author__ = 'kdq'
from app.models import AppUser
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