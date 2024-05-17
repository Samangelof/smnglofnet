from django.urls import path
from .views import (
    PostAPIList, 
    PostAPIUpdate,
    PostAPIDestroy,
    CommentAPIList, 
    CommentAPIUpdate,
    CommentAPIDestroy
)


urlpatterns = [
    # ------------------------------------------------
    # POSTS
    path('api/v6/posts/', PostAPIList.as_view()),
    path('api/v6/post_update/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v6/post_delete/<int:pk>/', PostAPIDestroy.as_view()),

    # ------------------------------------------------
    # COMMENTS
    path('api/v7/comments/', CommentAPIList.as_view()),
    path('api/v7/comment_update/<int:pk>/', CommentAPIUpdate.as_view()),
    path('api/v7/comment_delete/<int:pk>/', CommentAPIDestroy.as_view()),
]