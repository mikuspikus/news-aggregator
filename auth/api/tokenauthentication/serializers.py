from rest_framework import serializers

class TokenSerializer(serializers.Serializer):
    ID = ''
    SECRET = ''

    id = serializers.CharField(label = 'id')
    secret = serializers.CharField(label = 'secret')

    def __validate(self, id: str, secret: str) -> bool:
        return self.ID == id and self.SECRET == secret

    def validate(self, attrs: dict) -> dict:
        id_, secret = attrs.get('id'), attrs.get('secret')

        if id_ and secret:
            is_valid = self.__validate(id_, secret)

            if not is_valid:
                msg = 'Invalid \'id\' or \'secret\''
                raise serializers.ValidationError(msg, code = 'authorization')


        else:
            msg = 'Params \'id\' or \'secret\' not found'
            raise serializers.ValidationError(msg, code = 'authorization')

        return attrs
