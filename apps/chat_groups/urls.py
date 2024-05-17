from django.urls import path, include
from .views import UserGroupChatAPIList


urlpatterns = [
    # ------------------------------------------------
    # MESSAGE IN GROUP
    path('api/v5/chat_group', UserGroupChatAPIList.as_view()),
]