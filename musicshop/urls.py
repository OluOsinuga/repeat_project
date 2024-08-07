from django.urls import path

from . import views

app_name= 'musicshop'
urlpatterns =[
    path('',views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/' ,views.product_detail, name= 'product_detail'),
]