from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense,Category
from .serializer import ExpenseSerializer,CategorySerializer
from rest_framework import status,viewsets
from django.shortcuts import get_object_or_404
from .utils import success_response, error_response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['amount', 'date']

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(success_response("Expenses fetched successfully", response.data))

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(success_response("Expense fetched successfully", response.data))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(success_response("Expense created successfully", serializer.data), status=status.HTTP_201_CREATED)
        return Response(error_response("Validation failed", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response("Expense updated successfully", serializer.data))
        return Response(error_response("Validation failed", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(success_response("Expense deleted successfully"), status=status.HTTP_204_NO_CONTENT)
        
class ExpenseSummaryView(APIView):
    def get(self,request):
        expense=Expense.objects.filter(user=request.user)
        total_count=expense.count()
        total_amount=0
        for expens in expense:
            total_amount+=expens.amount
        highest = expense.order_by('-amount').first()
        highest_data = ExpenseSerializer(highest).data  
        return Response(
        success_response("Summary fetched successfully", {
        "total_expenses": total_count,
        "total_amount": total_amount,
        "highest_expense": highest_data
    })
)
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)