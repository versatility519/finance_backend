from django.urls import path
from .views import (
    SupplierListCreateView,
    SupplierDetailView,
    ContactListCreateView,
    ContactDetailView,
    InvoiceListCreateView,
    InvoiceDetailView,
    InvoiceItemListCreateView,
    InvoiceItemDetailView,
    DocumentListCreateView,
    DocumentDetailView,
    TaxInfoListCreateView,
    TaxInfoDetailView,
    TermsListCreateView,
    TermsDetailView,
)

urlpatterns = [
    path('suppliers', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier-detail'),
    
    path('contacts', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    
    path('invoices', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    
    path('invoiceitem', InvoiceItemListCreateView.as_view(), name='invoiceitem-list-create'),
    path('invoiceitem/<int:pk>', InvoiceItemDetailView.as_view(), name='invoiceitem-detail'),

    path('documents', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>', DocumentDetailView.as_view(), name='document-detail'),
    
    path('taxInfo', TaxInfoListCreateView.as_view(), name='taxinfo-list-create'),
    path('taxInfo/<int:pk>', TaxInfoDetailView.as_view(), name='taxinfo-detail'),
    
    path('terms', TermsListCreateView.as_view(), name='terms-list-create'),
    path('terms/<int:pk>', TermsDetailView.as_view(), name='terms-detail'),
]
