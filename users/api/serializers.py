from .models import User
from .requesters import send_credentials, update_credentials

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff']

        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop('password')

        new_user = User.objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        credentials = {'username' : validated_data['username'], 'password' : password, 'uuid' : str(new_user.id), 'is_staff': new_user.is_staff}

        response, code = send_credentials(credentials = credentials)

        if code != 201:
            new_user.delete()

            msg = response.get('error', str(response))
            raise serializers.ValidationError(msg)

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

        if validated_data.get('is_staff'):
            is_staff = validated_data.pop('is_staff')
            credentials['is_staff'] = is_staff
            instance.is_staff = is_staff

        if validated_data.get('email'):
            new_email = validated_data.pop('email')
            instance.email = new_email

        if credentials:
            response, code = update_credentials(uuid = instance.id, credentials = credentials)

            if code != 200:
                msg = response.get('error', '')
                raise serializers.ValidationError(msg)

        instance.save()
        return instance
