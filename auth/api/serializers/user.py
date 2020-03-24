from ..models import AuthUser

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = 'id', 'uuid', 'username', 'password'

        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data: dict) -> AuthUser:
        password = validated_data.pop('password')

        new_user = AuthUser.objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def update(self, instance: AuthUser, validated_data: dict) -> AuthUser:
        if validated_data.get('username'):
            new_username = validated_data.pop('username')
            instance.username = new_username

        if validated_data.get('password'):
            new_password = validated_data.pop('password')
            instance.set_password(new_password)

        instance.save()
        return instance
