#coding=utf-8
__author__ = 'kdq'
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.core.mail import send_mail
from django.core.cache import cache
from app.models import User, AppUser
import datetime


class SendMail(APIView):
    def post(self, request, format=None):
        code = random.randint(1000, 9999)
        subject = 'FieldInHand邮箱验证'
        from_email = 'justtempuse@163.com'
        to = request.data['email']
        text_content = '您的验证码是%s,请在30分钟内完成验证！'%code

        try:
            send_mail(subject, text_content, from_email, [to], fail_silently=False)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        cache.set(to+'code', code, 1800)
        return Response(status=status.HTTP_200_OK)


class CheckCode(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        code = request.data['code']
        code1 = cache.get(email+'code')
        if code1 is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if int(code1) != int(code):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


class Register(APIView):
    def post(self, requests, format=None):
        username = requests.data['username']
        password = requests.data['password']
        try:
            user = User.objects.get(username=username)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            user = User.objects.create_user(username=username, password=password,
                                            last_login=datetime.datetime.now(), email=username)
            user.save()
            appuser = AppUser()
            appuser.user = user
            appuser.save()
            return Response(status=status.HTTP_201_CREATED)