from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class categorySerializers(serializers.ModelSerializer):
	
	class Meta:
		model = Category
		fields = '__all__'
	

class subcategorySerializers(serializers.ModelSerializer):
	
	class Meta:
		model = Sub_Category
		fields = '__all__'

class productSerializers(serializers.ModelSerializer):
	
	class Meta:
		model = Product
		fields = '__all__'
		