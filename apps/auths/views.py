from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, views, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from djoser.conf import settings
from djoser import utils

from .models import UserNet
from .serializer import UserSerializer
from .permissions import IsOwnerOrReadOnly



class UserAPIList(generics.ListCreateAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (IsOwnerOrReadOnly,)


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class UserAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)



# class TokenDestroyView(views.APIView):
#     permission_classes = settings.PERMISSIONS.token_destroy
#     def post(self, request):
#         utils.logout_user(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)


def ViewAllUsers(request):
    template_name = 'api.html'
    return render(request, template_name=template_name)