from django.contrib import admin
from .models import Profile, Wallet

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'avatar')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'payment_method', 'setting')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Wallet, WalletAdmin)
