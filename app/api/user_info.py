__author__ = 'kdq'
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializer import AppUserSerializer
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_condition import Or

class UserInfo(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    required_scopes = ['read','write']
    def get(self, request, format=None):
        serializer = AppUserSerializer(request.user.appuser)
        return Response({"user":serializer.data}, status=status.HTTP_200_OK)
