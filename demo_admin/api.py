from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import math, random
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import *
import os


class categoryviewsets(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = categorySerializers
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	
class subcategoryviewsets(viewsets.ModelViewSet):
	queryset = Sub_Category.objects.all()
	serializer_class = subcategorySerializers
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]

class productviewsets(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = productSerializers
	# authentication_classes=[TokenAuthentication]
	# permission_classes=[IsAuthenticated]
	