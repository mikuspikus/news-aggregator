from rest_framework import serializers
from .models import GenericStat


class GenericStatSerializer(serializers.ModelSerializer):
    input = serializers.JSONField(required=False, allow_null=True)
    output = serializers.JSONField(required=False, allow_null=True)

    class Meta:
        model = GenericStat
        fields = '__all__'
