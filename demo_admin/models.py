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


class Sub_Category(models.Model):
    category_id=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    sub_category_name=models.CharField(max_length=10,null=True,blank=True)
    sub_category_image=models.ImageField(upload_to='images',null=True,blank=True)
    sub_category_code=models.CharField(max_length=10,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)


class Product(models.Model):
    product_name=models.CharField(max_length=10,null=True,blank=True)
    product_sku=models.CharField(max_length=10,null=True,blank=True,unique=True)
    product_size=models.CharField(max_length=10,null=True,blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='images',null=True,blank=True)

    category_id=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    sub_category_id=models.ForeignKey(Sub_Category,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
