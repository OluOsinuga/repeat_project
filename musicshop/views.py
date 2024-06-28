from django.views.generic import ListView
from .models import Product
# Create your views here.
class ShopListView(ListView):
    model = Product
    template_name='home.html'
    context_object_name ='all_products_list'