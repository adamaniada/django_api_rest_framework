from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import permissions
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        transaction = Transaction.objects.filter(user = request.user.id)
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'trans_id': "company_name",
            'trans_amount': request.data.get('trans_amount'), 
            'wallet_balance': request.data.get('wallet_balance'), 
            'you_give': request.data.get('you_give'), 
            'you_receive': request.data.get('you_receive'), 
            'exchange_amount': request.data.get('exchange_amount'), 
            'jamb_to_receive': request.data.get('jamb_to_receive'), 
            'code_otp': request.data.get('code_otp'),
            'wallet_id': request.data.get('wallet_id'),
            'wallet_new_balance': request.data.get('wallet_new_balance'), 
            'billed_date': request.data.get('billed_date'), 
            'status': request.data.get('status'), 
            'paid_date': request.data.get('paid_date'),
            'updated_at': request.data.get('updated_at'),
            'user': request.user.id
        }
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TransactionDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Transaction.objects.get(id=todo_id, user = user_id)
        except Transaction.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieves the Transaction with given todo_id
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with transaction id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TransactionSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
        Updates the transaction item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with transaction id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'trans_id': "company_name",
            'trans_amount': request.data.get('trans_amount'), 
            'wallet_balance': request.data.get('wallet_balance'), 
            'you_give': request.data.get('you_give'), 
            'you_receive': request.data.get('you_receive'), 
            'exchange_amount': request.data.get('exchange_amount'), 
            'jamb_to_receive': request.data.get('jamb_to_receive'), 
            'code_otp': request.data.get('code_code_otp'), 
            'wallet_id': request.data.get('wallet_id'),
            'wallet_new_balance': request.data.get('wallet_new_balance'), 
            'billed_date': request.data.get('billed_date'), 
            'status': request.data.get('status'), 
            'paid_date': request.data.get('paid_date'),
            'updated_at': request.data.get('updated_at'),
            'user': request.user.id
        }
        serializer = TransactionSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Deletes the transaction item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with transaction id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    

def api_v1_documentation(request, *args, **kwargs):
        return render(request, "api_v1/docs.html")
