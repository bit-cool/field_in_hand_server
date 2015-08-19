__author__ = 'kdq'
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from field_in_hand_server import settings
import requests
from oauth2_provider.models import Application
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_condition import Or
from django.views.decorators.csrf import csrf_exempt


class Logout(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    required_scopes = ['read','write']

    @csrf_exempt
    def get(self, request, format=None):
        try:
            username = request.user
            token = request.query_params["access_token"]
            app = settings.OAUTH_APPLICATION_NAME
            app = Application.objects.get(name=app)
            url = settings.OAUTH2_REVOKE_TOKEN_URL
            payload = {
                "token":token,
                "token_type_hint":"access_token",
                "client_id":app.client_id,
                "client_secret":app.client_secret,
            }
            r = requests.post(url, data=(payload))
            if r.status_code == 200:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status =status.HTTP_200_OK)