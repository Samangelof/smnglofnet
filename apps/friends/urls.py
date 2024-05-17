from django.urls import path, include

from .models import Follow
from .views import FollowApiList, FollowApiCreate, UserFollowing



urlpatterns = [
    # ------------------------------------------------
    # VIEW ALL FOLLOWS
    path('api/v3/all_follows/', FollowApiList.as_view()),
    
    # ------------------------------------------------
    # ADD FOLLOWS
    path('api/v3/add_follows/', FollowApiCreate.as_view()),

    # ------------------------------------------------
    # USER FOLLOWERS
    path('api/v3/user_follows/', UserFollowing.as_view()),
    
]



