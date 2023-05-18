from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default="avatar.jpg")
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    payment_method = models.JSONField() # method, balance, devise
    setting = models.JSONField() # method

    def __str__(self):
        return self.user_id