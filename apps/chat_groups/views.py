from django.shortcuts import render
from rest_framework import generics

from .models import UserSendMessageInGroup
from .permissions import IsOwnerOrReadOnly
from .serializer import UserMessageGroupSerializer

class UserGroupChatAPIList(generics.ListCreateAPIView):
    queryset = UserSendMessageInGroup.objects.all()
    serializer_class = UserMessageGroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)



