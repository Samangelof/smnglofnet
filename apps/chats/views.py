from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Messages
from .serializers import MessageSerializer
from .permissions import IsOwnerForMessageReadOnly, PrivateMessageReadonly



class MessageAPIList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


class MessageAPIUpdate(generics.UpdateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


class MessageAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )




class MessagesAPIPrivate(generics.ListCreateAPIView):
    def get(self, request, user_name):
        # m = UserNet.objects.filter(sender__username='Tekken')
        m = Messages.objects.filter(sender__username=user_name)
        m2 = Messages.objects.filter(receiver__username=user_name)
        
        return Response({
            'messages_sender': MessageSerializer(m, many=True).data,
            'message_receiver': MessageSerializer(m2, many=True).data
        })

    serializer_class = MessageSerializer
    permission_classes = (PrivateMessageReadonly,)
