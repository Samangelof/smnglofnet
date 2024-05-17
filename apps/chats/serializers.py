from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserNet, Messages


class UserNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserNet
        fields = ("username", "email", "first_name", "last_name", "avatar", "phone")


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())

    class Meta:
        model = Messages
        fields = ['sender', 'receiver', 'message', 'data_send']