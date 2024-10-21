from django.urls import include, path
from .views import (LegerAccDetailView, LegerAccListCreateView)

urlpatterns = [
    path('LegerAcc', LegerAccListCreateView.as_view(), name='supplier-list-create'),
    path('LegerAcc/<int:pk>', LegerAccDetailView.as_view(), name='supplier-detail'),
]