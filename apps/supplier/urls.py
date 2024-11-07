from django.urls import path
from .views import (
    SupplierListCreateView, 
    SupplierDetailView,
    SupplierItemListCreateView,
    SupplierItemDetailView,
    SupplierContactListCreateView,
    SupplierContactDetailView,
)
urlpatterns = [
    path('suppliers', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier-detail'),

    path('supplier-items', SupplierItemListCreateView.as_view(), name='supplier-item-list-create'),
    path('supplier-items/<int:pk>', SupplierItemDetailView.as_view(), name='supplier-item-detail'),

    path('supplier-contacts', SupplierContactListCreateView.as_view(), name='supplier-contact-list-create'),
    path('supplier-contacts/<int:pk>', SupplierContactDetailView.as_view(), name='supplier-contact-detail'),

]


