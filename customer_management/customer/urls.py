from django.urls import path
from .views import (
    CustomerListCreateAPIView,
    CustomerRetrieveUpdateDestroyAPIView,
    CustomerBulkUpdateAPIView,
    CustomerBulkDeleteAPIView,
)

urlpatterns = [
    # List all customers or create a new record
    path('customers/', CustomerListCreateAPIView.as_view(), name='customers-list-create'),
    # Retrieve, update, or delete a customer by id
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    # Bulk update: update all customers
    path('customers/updateAll/', CustomerBulkUpdateAPIView.as_view(), name='customers-bulk-update'),
    # Bulk delete: delete all customers
    path('customers/deleteAll/', CustomerBulkDeleteAPIView.as_view(), name='customers-bulk-delete'),
]