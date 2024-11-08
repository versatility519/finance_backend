from django.urls import include, path
from .views import (
    LegerAccountListCreateView,
    LegerAccountDetailView,
    
    SubSAccountListCreateView,
    SubSAccountDetailView,

    SubAccountListCreateView,
    SubAccountDetailView,
)

urlpatterns = [
    path('leger-account', LegerAccountListCreateView.as_view(), name='supplier-list-create'),
    path('leger-account/<int:pk>', LegerAccountDetailView.as_view(), name='supplier-detail'),
    
    path('subs-account', SubSAccountListCreateView.as_view(), name='subaccount-list-create'),
    path('subs-account/<int:pk>', SubSAccountDetailView.as_view(), name='subaccount-detail'),
    
    path('subaccount', SubAccountListCreateView.as_view(), name='subaccount-list-create'),
    path('subaccount/<int:pk>', SubAccountDetailView.as_view(), name='subaccount-detail'),
]