from django.contrib import admin
from .models import Transaction

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('trans_amount' , 'you_give', 'you_receive', 'exchange_amount', 'jamb_to_receive', 'code_otp', 'wallet_id', 'wallet_new_balance', 'billed_date', 'status', 'paid_date', 'updated_at')

admin.site.register(Transaction, TransactionAdmin)
