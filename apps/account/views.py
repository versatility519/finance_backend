from rest_framework import generics, status
from rest_framework.response import Response
from .models import LedgerAccount, SubAccount
from .serializers import LedgerAccountSerializer

class LedgerAccountCreateListView(generics.ListCreateAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer

    def post(self, request, *args, **kwargs):
        account_data = request.data
        
        # Extract depth and num_sub_accounts
        depth = int(account_data.get("depth", 1))  # default depth is 1
        num_sub_accounts = int(account_data.get("num_sub_accounts", 1))  # default num_sub_accounts is 1
        
        # Prepare data for LedgerAccount creation
        ledger_account_data = {
            "ledger_name": account_data.get("ledger_name"),
            "account_type": account_data.get("account_type"),
            "status_change": account_data.get("status_change"),
            "sub_accounts": self._generate_sub_accounts(num_sub_accounts, depth)
        }

        # Serialize and save the LedgerAccount
        serializer = LedgerAccountSerializer(data=ledger_account_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _generate_sub_accounts(self, num_sub_accounts, depth, current_depth=1):
        # If current_depth exceeds depth, return empty list
        if current_depth > depth:
            return []
        
        sub_accounts = []
        for i in range(num_sub_accounts):
            sub_account_data = {
                "name": f"SubAccount Level {current_depth} - {i+1}",
                "ledger_account": None,  # Will be assigned when saving the root LedgerAccount
                "parent": None  # Parent will be assigned recursively
            }
            
            # Recursively create children for the sub-accounts
            sub_account_data["children"] = self._generate_sub_accounts(num_sub_accounts, depth, current_depth + 1)
            sub_accounts.append(sub_account_data)
        
        return sub_accounts

class LedgerAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer
 
