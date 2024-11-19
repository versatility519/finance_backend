from django.urls import path
from .views import (
    CarrierListCreateView, 
    CarrierDetailView,
    
    SupplierListCreateView, 
    SupplierDetailView,
    
    SupplierItemListCreateView,
    SupplierItemDetailView,
    
    SupplierContactListCreateView,
    SupplierContactDetailView,
    
    ShippingItemCreateView,
    ShippingItemDetailView,
    
    ShipDocsCreateView,
    ShipDocsDetailView,
    
    ShippingCreateView,
    ShippingDetailView,
    
    SupplierPOCreateView,
    SupplierPODetailView,
)
urlpatterns = [
    path('carriers', CarrierListCreateView.as_view(), name='carrier-list-create'),
    path('carriers/<int:pk>', CarrierDetailView.as_view(), name='carrier-detail'),

    path('suppliers', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier-detail'),

    path('supplier-items', SupplierItemListCreateView.as_view(), name='supplier-item-list-create'),
    path('supplier-items/<int:pk>', SupplierItemDetailView.as_view(), name='supplier-item-detail'),

    path('supplier-contacts', SupplierContactListCreateView.as_view(), name='supplier-contact-list-create'),
    path('supplier-contacts/<int:pk>', SupplierContactDetailView.as_view(), name='supplier-contact-detail'),

    path('shipping-items', ShippingItemCreateView.as_view(), name='shipping-item-create'),
    path('shipping-items/<int:pk>', ShippingItemDetailView.as_view(), name='shipping-item-detail'),

    path('ship-docs', ShipDocsCreateView.as_view(), name='ship-docs-create'),
    path('ship-docs/<int:pk>', ShipDocsDetailView.as_view(), name='ship-docs-detail'),

    path('shipping', ShippingCreateView.as_view(), name='shipping-create'),
    path('shipping/<int:pk>', ShippingDetailView.as_view(), name='shipping-detail'),

    path('supplier-po', SupplierPOCreateView.as_view(), name='supplier-po-create'),
    path('supplier-po/<int:pk>', SupplierPODetailView.as_view(), name='supplier-po-detail'),
]

