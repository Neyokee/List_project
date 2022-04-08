from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.main_listing, name = 'main_listing'),
    path('', views.auth_view, name = ''),
    path('main_list', views.main_listing, name = 'main_listing'),
    path('prod/<int:pk>/', views.product_list, name = 'products'),
    path('addlist', AddListView.as_view(), name='addlist_url'),
    path('addproduct', AddProductView.as_view(), name='addproduct_url'),
    path('register', UserFromView.as_view(), name = 'register_url'),
    path('login/', views.auth_view, name = 'login_url'),
    path('logout', views.auth_logout, name ='logout_url'),
    path('successful', views.successful, name = 'suc_url')
    # path('login', views.login_view(), name = 'login')
    # path('productsedit', ProductEditVies.as_view(), name = 'product_edit_url')

]

