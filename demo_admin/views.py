from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login , logout
from django. contrib import messages
from demo_admin.models import * 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
import json
import os
from django.core import serializers

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




##############################################  category funtions ##########################################


def category_show(request):
    cat_obj=Category.objects.all()
    context={'cat_obj':cat_obj}

    return render(request,'admin_template/category/category-show.html',context)

def category_add(request):
    if request.method == 'POST':
        if(request.POST['cat_id']!=''):
            category=Category.objects.get(id=request.POST['cat_id'])
        else:
            category=Category()

        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')

        category_code = request.POST.get('category_code')
        print(category_image,'category_image')
        if(category_image!=None):
            category.category_image=category_image
        category.category_name=category_name
        
        category.category_code=category_code
        
        category.save()
        return JsonResponse({'result': 'success'})
    else:
        return render(request,'admin_template/category/category.html')
    
def category_update(request,id):
    category_obj=Category.objects.get(id=id)
    context={
        'category_obj':category_obj
    }
    return render(request,'admin_template/category/category.html',context=context)


def category_delete(request,id):
    category_obj=Category.objects.get(id=id)
    if category_obj.category_image.name!="":
                os.remove(category_obj.category_image.path)
    category_obj.delete()
    return redirect('category_show')


##############################################  sub category funtions ##########################################

def show_subcategory(request):
    data=Sub_Category.objects.all()
    context={'data':data}
    return render(request,'admin_template/sub_category/show_subcategory.html',context)


def add_subcategory(request):
    if request.method == 'POST':
        if request.POST['sub_cat_id']!="":
            sub_category=Sub_Category.objects.get(id=request.POST['sub_cat_id'])
        else:
            sub_category=Sub_Category()

        sub_category_name = request.POST.get('sub_category_name')
        sub_category_image = request.FILES.get('sub_category_image')
        sub_category_code = request.POST.get('sub_category_code')

        category_id = request.POST.get('category_id')
        cat_obj=Category.objects.get(id=category_id)
        
        

        sub_category.sub_category_name=sub_category_name
        if(sub_category_image!=None):
            sub_category.sub_category_image=sub_category_image
        sub_category.sub_category_code=sub_category_code

        sub_category.category_id=cat_obj

        sub_category.save()
        # return redirect('show_subcategory')
        return JsonResponse({'result': 'success'})
    else:
        cat_obj=Category.objects.all()
        context={'cat_obj':cat_obj}
        return render(request,'admin_template/sub_category/add_subcategory.html',context=context)

def edit_subcategory(request,id):
    sub_cat_obj=Sub_Category.objects.get(id=id)
    cat_obj=Category.objects.all()
    context={
        "sub_cat_obj":sub_cat_obj,
        'cat_obj':cat_obj
    }
    return render(request,'admin_template/sub_category/add_subcategory.html',context=context)


def delete_subcategory(request,id):
    subcategory_obj=Sub_Category.objects.get(id=id)
    if subcategory_obj.sub_category_image.name!="":
                os.remove(subcategory_obj.sub_category_image.path)
    subcategory_obj.delete()
    return redirect('show_subcategory')

##############################################  products funtions ##########################################

def show_product(request):
    data=Product.objects.all()
    context={'data':data}
    return render(request,'admin_template/product/show_product.html',context)


def add_product(request):
    if request.method == 'POST':
        if(request.POST['pro_id']!=''):
            product=Product.objects.get(id=request.POST['pro_id'])
            print("inside if")
        else:
            product=Product()
            print("inside else")
            
        # product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_sku = request.POST.get('product_sku')
        product_size = request.POST.get('product_size')
        print()
        price = request.POST.get('price')
        images = request.FILES.get('product_image')
       
        category_id = request.POST.get('cat_id')
        print(category_id,'category_id')
        cat_obj=Category.objects.get(id=category_id)

        try:
            sub_category_id = request.POST.get('sub_cat_id')
            sub_cat_obj=Sub_Category.objects.get(id=sub_category_id)
            product.sub_category_id=sub_cat_obj
        except:
            pass
       
        

        # status_obj=Status.objects.get(id=product_status)

        
        # product.product_id=product_id
        product.product_name=product_name
        product.product_sku=product_sku
        product.product_size=product_size
        product.price=price
        if(images!=None):
            product.images=images

        # product.product_status=product_status
       
        product.category_id=cat_obj
        
        # product.brand_id=brand_obj
       

        product.save()
        return JsonResponse({'result': 'success'})
    else:

        cat_obj=Category.objects.all()
        sub_cat_obj=Sub_Category.objects.all()
        # status_obj=Category.objects.filter(category_status='Active')
        # brand_obj=Brand.objects.all()
        

        c={ 'cat_obj':cat_obj,
            'sub_cat_obj':sub_cat_obj,
          }
        return render(request,'admin_template/product/add_product.html',c)
    

def edit_product(request,id):
    pro_obj=Product.objects.get(id=id)
    cat_obj=Category.objects.all()
    sub_cat_obj=Sub_Category.objects.all()
    context={
        "pro_obj":pro_obj,
        'cat_obj':cat_obj,
        'sub_cat_obj':sub_cat_obj,
    }
    return render(request,'admin_template/product/add_product.html',context)

def delete_product(request,id):
    pro_obj=Product.objects.get(id=id)
    pro_obj.delete()
    return redirect('show_product')
def getproduct(request):
    if request.method=='GET':
        category_id=request.GET['category_name']
        
        cat_obj=Category.objects.get(id=category_id)
        sub_cat_obj=serializers.serialize('json',Sub_Category.objects.filter(category_id=cat_obj))

        print(sub_cat_obj,'aaaaaaa')
        return HttpResponse(sub_cat_obj)

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



def sub_cat_code_vali(request):
    sub_category_code = request.POST.get('sub_category_code')
     
    if(sub_category_code!=''):
        if Sub_Category.objects.filter(sub_category_code=sub_category_code).exists():
            return HttpResponse('<div id="checksubcode" value="This Code is already exists" style="color: red"> This Code is already exists </div>')
        else:   
            return HttpResponse('<div id="checksubcode" value="" style="color: green"></div>')
    else:
        return HttpResponse('<div id="checksubcode" value="" style="color: green"></div>')
    

def pro_sku_vali(request):
    product_sku = request.POST.get('product_sku')
     
    if(product_sku!=''):
        if Product.objects.filter(product_sku=product_sku).exists():
            return HttpResponse('<div id="checksku" value="This SKU Code is already exists" style="color: red"> This SKU Code is already exists </div>')
        else:   
            return HttpResponse('<div id="checksku" value="" style="color: green"></div>')
    else:
        return HttpResponse('<div id="checksku" value="" style="color: green"></div>')