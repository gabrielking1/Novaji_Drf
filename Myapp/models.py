from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



class Registration(models.Model):
   

    ref_code = models.CharField(max_length=20, unique=True, blank=True)  
    mobile_network = models.CharField(max_length=20, unique=True, blank=True)
    
    phone_number = PhoneNumberField(blank=True, max_length=15)
   
   
   

  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.ref_code:
            self.ref_code = get_random_string(16).upper()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"Coupon {self.code} for {self.store}"
