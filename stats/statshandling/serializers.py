from rest_framework import serializers
from .models import GenericStat


class GenericStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericStat
        fields = '__all__'
