from django.urls import path
from .views import generate_invoice

urlpatterns = [
    path('', generate_invoice, name='generate-pdf'),
]
