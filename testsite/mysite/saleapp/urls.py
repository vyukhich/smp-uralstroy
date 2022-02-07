from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('catalog/', catalog, name='catalog_url'),
    path('calculator/', calc, name='calc_url')
]