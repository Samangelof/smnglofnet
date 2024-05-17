from rest_framework import serializers
from .models import UserNet


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserNet
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'password')

        def create(self, validated_data):
            return UserNet.objects.create_user(
                validated_data['username'], None, validated_data['password'])