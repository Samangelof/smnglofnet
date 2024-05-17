from rest_framework import serializers
from .models import UserSendMessageInGroup


class UserMessageGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSendMessageInGroup
        fields = ('user_sender', 'message', 'receiver_group',)