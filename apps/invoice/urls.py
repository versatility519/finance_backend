from django.urls import path
from .views import (
    InvoiceListCreateView,
    InvoiceDetailView,
    InvoiceItemListCreateView,
    InvoiceItemDetailView,
    InvoiceDocListCreateView,
    InvoiceDocDetailView,
    TermsListCreateView,
    TermsDetailView,
)

urlpatterns = [ 
 
    path('invoices', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    
    path('invoice-item', InvoiceItemListCreateView.as_view(), name='invoiceitem-list-create'),
    path('invoice-item/<int:pk>', InvoiceItemDetailView.as_view(), name='invoiceitem-detail'),

    path('invoice-doc', InvoiceDocListCreateView.as_view(), name='invoicedoc-list-create'),
    path('invoice-doc/<int:pk>', InvoiceDocDetailView.as_view(), name='invoicedoc-detail'),
    
    path('terms', TermsListCreateView.as_view(), name='terms-list-create'),
    path('terms/<int:pk>', TermsDetailView.as_view(), name='terms-detail'),
]
