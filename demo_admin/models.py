from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.



class Category(models.Model):
    category_name=models.CharField(max_length=10,null=True,blank=True)
    category_image=models.ImageField(upload_to='images',null=True,blank=True)
    category_code=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
