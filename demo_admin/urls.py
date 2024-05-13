from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from demo_admin import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.start_up,name='start_up'),

    path('login/',views.admin_login,name='admin_login'),
    path('logout/', views.admin_logout, name='logout'),

#################################### category ###################################################3
    path('category_show/', views.category_show, name='category_show'),
    path('category_add/', views.category_add, name='category_add'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),

################################ sub category ######################################
    path('show_subcategory/', views.show_subcategory, name='show_subcategory'),
    path('add_subcategory/', views.add_subcategory, name='add_subcategory'),
    path('edit_subcategory/<int:id>', views.edit_subcategory, name='edit_subcategory'),
    path('delete_subcategory/<int:id>', views.delete_subcategory, name='delete_subcategory'),
    # path('change_subcategory_status/<id>', views.change_subcategory_status, name='change_subcategory_status'),
    path('checksubcode/', views.sub_cat_code_vali, name='checksubcode'),

################################ products ######################################
    path('getproduct/', views.getproduct, name='getproduct'),
    path('show_product/', views.show_product, name='show_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<id>', views.edit_product, name='edit_product'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),
    path('checksku/', views.pro_sku_vali, name='checksku'),

#################################### validations #####################################
    path('checkcode/', views.cat_code_vali, name='checkcode'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)