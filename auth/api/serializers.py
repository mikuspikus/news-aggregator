from .models import AuthServiceToken, UsersServiceToken, RSSParserServiceToken, CommentsServiceToken, NewsServiceToken, StatsServiceToken
from .tokenauthentication.serializers import TokenSerializer

from rest_framework import serializers

from django.conf import settings

class AuthServiceTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['AUTH']['ID']
    SECRET = settings.CREDENTIALS['AUTH']['SECRET']

class UsersServiceTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['USERS']['ID']
    SECRET = settings.CREDENTIALS['USERS']['SECRET']

class CommentsServiceTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['COMMENTS']['ID']
    SECRET = settings.CREDENTIALS['COMMENTS']['SECRET']

class RSSPareserServiceTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['RSS-PARSER']['ID']
    SECRET = settings.CREDENTIALS['RSS-PARSER']['SECRET']

class NewsTokenServiceSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['NEWS']['ID']
    SECRET = settings.CREDENTIALS['NEWS']['SECRET']

class StatsTokenServiceSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['STATS']['ID']
    SECRET = settings.CREDENTIALS['STATS']['SECRET']