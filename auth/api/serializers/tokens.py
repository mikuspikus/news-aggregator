from tokenauthentication.serializers import TokenSerializer

from django.conf import settings


class ServicesTokenSerializer(TokenSerializer):
    CREDENTIALS = settings.CREDENTIALS
