from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    trans_id = models.CharField(max_length=180, default="COMPANY_NAME")
    wallet_id = models.IntegerField()
    wallet_balance = models.IntegerField()
    trans_amount = models.IntegerField()
    wallet_new_balance = models.IntegerField()
    you_give = models.CharField(max_length=180)
    you_receive = models.CharField(max_length=180)
    exchange_amount = models.IntegerField()
    jamb_to_receive = models.IntegerField()
    code_otp = models.CharField(max_length=6)
    billed_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    status = models.BooleanField(default = False, blank = True)
    paid_date = models.DateTimeField(auto_now = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.jamb_to_receive
