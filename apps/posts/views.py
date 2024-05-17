from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostPersonalSerializer, CommentPersonalSerializer
from .models import PostInPersonAccount, CommentOnPersonalAccount
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class PostAPIList(generics.ListCreateAPIView):
    queryset = PostInPersonAccount.objects.all()
    serializer_class = PostPersonalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PostInPersonAccount.objects.all()
    serializer_class = PostPersonalSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PostInPersonAccount.objects.all()
    serializer_class = PostPersonalSerializer
    permission_classes = (IsAdminOrReadOnly,)





class CommentAPIList(generics.ListCreateAPIView):
    queryset = CommentOnPersonalAccount.objects.all()
    serializer_class = CommentPersonalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentAPIUpdate(generics.UpdateAPIView):
    queryset = CommentOnPersonalAccount.objects.all()
    serializer_class = CommentPersonalSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = CommentOnPersonalAccount.objects.all()
    serializer_class = CommentPersonalSerializer
    permission_classes = (IsAdminOrReadOnly,)