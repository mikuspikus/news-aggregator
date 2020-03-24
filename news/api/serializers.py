from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('votes',)
        read_only_fields = ('score',)