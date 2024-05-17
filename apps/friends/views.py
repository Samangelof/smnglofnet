from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.views import APIView, View
from rest_framework import generics
from rest_framework.response import Response


from auths.permissions import IsOwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer

try:
    from auths.models import UserNet
    user_model = UserNet

except ImportError:
    from django.contrib.auth.models import User
    user_model = User



class FollowApiList(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class FollowApiCreate(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsOwnerOrReadOnly,)



# USERS FOLLOWERS
class UserFollowing(APIView):
    def get(self, request):     # id(int) or user_name(slug)
        user_following = Follow.objects.filter(follower__username='Avdenago')
        # f = Follow.objects.filter(sender__username=user_name)

        return Response({'user_follower': FollowSerializer(user_following, many=True).data})





# def followers(request, username, template_name="friendship/follow/followers_list.html"):
#     """ List this user's followers """
#     user = get_object_or_404(user_model, username=username)
#     followers = Follow.objects.followers(user)
#     return render(
#         request,
#         template_name,
#         {
#             get_friendship_context_object_name(): user,
#             "friendship_context_object_name": get_friendship_context_object_name(),
#             "followers": followers,
#         },
#     )