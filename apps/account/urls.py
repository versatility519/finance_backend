from django.urls import include, path
from .views import (
    LegerAccListCreateView,
    LegerAccDetailView,

    SubAccountListCreateView,
    SubAccountDetailView,
)

urlpatterns = [
    path('leger-account', LegerAccListCreateView.as_view(), name='supplier-list-create'),
    path('leger-account/<int:pk>', LegerAccDetailView.as_view(), name='supplier-detail'),
    
    path('subaccount', SubAccountListCreateView.as_view(), name='subaccount-list-create'),
    path('subaccount/<int:pk>', SubAccountDetailView.as_view(), name='subaccount-detail'),
]