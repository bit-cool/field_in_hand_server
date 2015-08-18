__author__ = 'kdq'
from django.conf.urls import url
from api.login import Login

urlpatterns = [
    url('^login/',Login.as_view()),
]