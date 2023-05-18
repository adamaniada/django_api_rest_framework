from rest_framework import serializers
from .models import Transaction
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["trans_id" ,"trans_amount", "wallet_balance", "you_give", "you_receive", "exchange_amount", "jamb_to_receive", "code_otp", "wallet_id", "wallet_new_balance", "billed_date", "status", "paid_date", "updated_at", "user"]
