from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
from .serializer import ExpenseSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .utils import success_response, error_response

class ExpenseListView(APIView):
    def get(self,request):
        expenses=Expense.objects.filter(user=request.user)
        serializers=ExpenseSerializer(expenses,many=True)
        return Response(
            success_response("Expenses fetched successfully", serializers.data)
        )
    def post(self,request):
        serializer=ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                success_response("Expense created successfully", serializer.data),
                status=status.HTTP_201_CREATED
            )
        return Response(
            error_response("Validation failed", serializer.errors),
            status=status.HTTP_400_BAD_REQUEST
        )
class ExpenseDetailView(APIView):
    
    def get(self,request,pk):
        expense=get_object_or_404(Expense, pk=pk , user=request.user)
        serializer=ExpenseSerializer(expense)
        return Response(
            success_response("Expense fetched successfully", serializer.data)
        )
    def put(self,request,pk):
        expense=get_object_or_404(Expense,pk=pk , user=request.user)
        serializer=ExpenseSerializer(expense,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success_response("Expense updated successfully", serializer.data)
            )
        return Response(
            error_response("Validation failed", serializer.errors),
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request,pk):
        expense=get_object_or_404(Expense,pk=pk,user=request.user)
        expense.delete()
        return Response(
            success_response("Expense deleted successfully"),
            status=status.HTTP_204_NO_CONTENT
        )
        
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