from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):

    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'password', 'uuid'

        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data: dict) -> CustomUser:
        password = validated_data.pop('password')

        new_user = CustomUser.objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def update(self, instance: CustomUser, validated_data: dict) -> CustomUser:
        instance.username = validated_data.get('username', instance.username)

        if validated_data.get('password'):
            new_password = validated_data.pop('password')
            instance.set_password(new_password)

        instance.save()
        return instance
