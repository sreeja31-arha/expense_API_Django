from django.urls import path
from .views import ExpenseListView, ExpenseDetailView,ExpenseSummaryView

urlpatterns = [
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-details'),
    path('expenses/summary/', ExpenseSummaryView.as_view(), name='expense-summary'),
]