from django.urls import path
from .views import HomePageView
from . import views

app_name= 'musicshop'
urlpatterns =[
    path('home/',HomePageView.as_view(),name='home'),
    path('',views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/' ,views.product_detail, name= 'product_detail'),
]