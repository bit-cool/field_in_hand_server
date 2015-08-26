__author__ = 'kdq'
from django.conf.urls import url
from api.login import Login
from api.register import SendMail, CheckCode, Register
from api.logout import Logout
from api.user_info import UserInfo

urlpatterns = [
    url('^login/', Login.as_view()),
    url('^logout/', Logout.as_view()),
    url('^send_mail/', SendMail.as_view()),
    url('^check_code/', CheckCode.as_view()),
    url('^register/', Register.as_view()),
    url('^user_info/', UserInfo.as_view()),
]