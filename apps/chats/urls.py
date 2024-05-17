from django.urls import path
from .views import (
    MessageAPIList, 
    MessageAPIUpdate,
    MessageAPIDelete,
    MessagesAPIPrivate,
)


urlpatterns = [
    # ------------------------------------------------
    # MESSENGER
    path('api/v4/chat_all/', MessageAPIList.as_view()),
    path('api/v4/chat_update/<int:pk>/', MessageAPIUpdate.as_view()),
    path('api/v4/chat_delete/<int:pk>/', MessageAPIDelete.as_view()),

    path('api/v4/private_message/<slug:user_name>/', MessagesAPIPrivate.as_view()),
]