from .models import User
from .requester import UsersRequester

from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = 'id', 'username', 'password', 'email'

        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop('password')

        new_user = User.objects.create(**validated_data)
        new_user.set_password(password)

        credentials = {'username' : validated_data['username'], 'password' : validated_data['password']}

        response, code = UsersRequester().send_credentials(credentials)

        if code != 201:
            msg = response.get('error', '')
            raise serializers.ValidationError(msg)

        new_user.save()

        return new_user

    def update(self, instance: User, validated_data: dict) -> User:
        credentials = {}

        if validated_data.get('username'):
            new_username = validated_data.pop('username')
            credentials['username'] = new_username
            instance.username = new_username

        if validated_data.get('password'):
            new_password = validated_data.pop('password')
            credentials['password'] = instance.password
            instance.set_password(new_password)

        if validated_data.get('email'):
            new_email = validated_data.pop('email')
            instance.email = new_email

        if credentials:
            response, code = UsersRequester().update_credentials(credentials)

            if code != 200:
                msg = response.get('error', '')
                raise serializers.ValidationError(msg)

        instance.save()
        return instance
