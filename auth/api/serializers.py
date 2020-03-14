from .models import UsersToken, RSSParserToken, CommentsToken, NewsToken, StatsToken

from rest_framework.serializers import Serializer, ValidationError, CharField
class TokenSerializer(Serializer):
    ID = ''
    id = CharField(label = 'id')

    def validate(self, attrs: dict) -> dict:
        id_ = attrs.get('id')

        if id_:
            pass

        return attrs

class UsersTokenSerializer(TokenSerializer):
    ID = 'memes'

class CommentsTokenSerializer(TokenSerializer):
    ID = 'memes'

class RSSPareserTokenSerializer(TokenSerializer):
    ID = 'memes'

class NewsTokenSerializer(TokenSerializer):
    ID = 'memes'

class StatsTokenSerializer(TokenSerializer):
    ID = 'memes'