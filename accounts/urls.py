from django.urls import path
from musicshop import views
from .views import SignUpView

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
]