from django.urls import path
from .views import Razor_Pay, Success
urlpatterns = [
    path('', Razor_Pay , name='razorpay'),
    path('success', Success , name='success'),


]
