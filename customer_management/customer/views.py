from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, filters, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.pagination import PageNumberPagination


# Pagination class: 10 items per page by default
class CustomerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# List and Create endpoint with filtering, ordering, and pagination 
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.select_related().defer('modified_at').order_by('-created_at')
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    ordering_fields = ['first_name', 'last_name', 'age', 'created_at']
    ordering = ['-created_at']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# Retrieve, Update, and Delete a single record by ID
class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


# Bulk update: Update multiple records with the given data
class CustomerBulkUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, *args, **kwargs):
        update_data = request.data  # Expecting a list of objects with 'id' and fields to update
        
        if not isinstance(update_data, list):
            return Response({"error": "Expected a list of customer objects."}, status=status.HTTP_400_BAD_REQUEST)
        
        updated_customers = []
        for customer_data in update_data:
            customer_id = customer_data.get('id')
            if not customer_id:
                return Response({"error": "Each object must have an 'id' field."}, status=status.HTTP_400_BAD_REQUEST)
            
            customer = get_object_or_404(Customer, id=customer_id)
            serializer = CustomerSerializer(customer, data=customer_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                updated_customers.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(updated_customers, status=status.HTTP_200_OK)


# Bulk delete: Delete multiple or all records
class CustomerBulkDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        customer_ids = request.data.get('ids', None)  # Expecting a list of IDs

        if customer_ids:
            deleted_count, _ = Customer.objects.filter(id__in=customer_ids).delete()
        else:
            deleted_count, _ = Customer.objects.all().delete()

        if deleted_count == 0:
            return Response({'message': 'No customers found to delete.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': f'{deleted_count} customers deleted successfully.'}, status=status.HTTP_200_OK)
      