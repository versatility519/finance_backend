from django.urls import path
from .views import (
    UserCreateView, 
    UserListView, 
    UserInfoView,
    
    RegisterView, LoginView
)

urlpatterns = [
    path('usercreate', UserCreateView.as_view(), name='user-create'),
    path('userlist', UserListView.as_view(), name='user-list'),
    path('userinfo/<int:pk>', UserInfoView.as_view(), name='user-userinfo'),
    
    
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]