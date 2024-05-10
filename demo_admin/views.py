from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login , logout
from django. contrib import messages
from demo_admin.models import * 
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.

def start_up(request):
   return redirect('admin_login')

def dashboard(request):
    return render(request,'admin_template/dashboard.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user,"inside admin_login")
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else: 
            user= User.objects.get(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.warning(request,'invalid username or password')

                return redirect('admin_login')
            
    else:
        return render(request, 'admin_template/login.html')
    

def admin_logout(request):
    logout(request)
    return redirect('admin_login')



def category_show(request):
    cat_obj=Category.objects.all()
    context={'cat_obj':cat_obj}

    return render(request,'admin_template/category/category-show.html',context)

def category_add(request):
    if request.method == 'POST':
        print(request,'request')
        exit()
        category_name = request.POST.get('category_name')
        category_image = request.FILES['category_image']
        category_code = request.POST.get('category_code')
        

        category=Category()
        category.category_name=category_name
        category.category_image=category_image
        category.category_code=category_code
        
        category.save()
        return JsonResponse({'result': 'success'})
    else:
        return render(request,'admin_template/category/category.html')
    


##############################################  validations funtions ##########################################

def cat_code_vali(request):
    category_code = request.POST.get('category_code')
     
    if(category_code!=''):
        if Category.objects.filter(category_code=category_code).exists():
            return HttpResponse('<div id="checkcode" value="This Code is already exists" style="color:red"> This Code is already exists </div>')
        else:   
            return HttpResponse('<div id="checkcode" value="" style="color: green"></div>')
    else:
        return HttpResponse('<div id="checkcode" value="" style="color: green"></div>')