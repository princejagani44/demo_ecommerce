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


#################################### validations #####################################
    path('checkcode/', views.cat_code_vali, name='checkcode'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)