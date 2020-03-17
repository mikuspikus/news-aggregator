from .models import UsersToken, RSSParserToken, CommentsToken, NewsToken, StatsToken
from .tokenauthentication.serializers import TokenSerializer

from rest_framework import serializers

from django.conf import settings

class UsersTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['USERS']['ID']
    SECRET = settings.CREDENTIALS['USERS']['SECRET']

class CommentsTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['COMMENTS']['ID']
    SECRET = settings.CREDENTIALS['COMMENTS']['SECRET']

class RSSPareserTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['RSS-PARSER']['ID']
    SECRET = settings.CREDENTIALS['RSS-PARSER']['SECRET']

class NewsTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['NEWS']['ID']
    SECRET = settings.CREDENTIALS['NEWS']['SECRET']

class StatsTokenSerializer(TokenSerializer):
    ID = settings.CREDENTIALS['STATS']['ID']
    SECRET = settings.CREDENTIALS['STATS']['SECRET']