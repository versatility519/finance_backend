
from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('users', UserList.as_view(), name='user-list'),  # List and create users
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),  # Retrieve, update, delete user
]