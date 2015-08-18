__author__ = 'kdq'
from django.conf.urls import url
from api.login import Login
from api.register import SendMail, CheckCode


urlpatterns = [
    url('^login/', Login.as_view()),
    url('^send_mail/', SendMail.as_view()),
    url('^check_code/', CheckCode.as_view()),
]