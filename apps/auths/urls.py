from django.urls import path, include
from .views import UserAPIList, UserAPIUpdate, UserAPIDestroy, ViewAllUsers


urlpatterns = [
    # ------------------------------------------------
    # DEFAULT DRF AUTH
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    

    # ------------------------------------------------
    # USER VIEW / CREATE / UPDATE / DELETE
    path('api/v2/users/', UserAPIList.as_view()),
    path('api/v2/user_update/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v2/user_delete/<int:pk>/', UserAPIDestroy.as_view()),


    # ------------------------------------------------
    # PARSE API
    # path('api/parse/users/', ViewAllUsers, name='all_users')
]