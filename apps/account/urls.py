from django.urls import path
from .views import LedgerAccountCreateListView, LedgerAccountDetailView

urlpatterns = [
    path('ledger-accounts', LedgerAccountCreateListView.as_view(), name='ledgeraccount-list-create'),
    path('ledger-accounts/<int:id>', LedgerAccountDetailView.as_view(), name='ledgeraccount-detail'),
]
