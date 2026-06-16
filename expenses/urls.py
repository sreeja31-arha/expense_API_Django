from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, CategoryViewSet, ExpenseSummaryView

router = DefaultRouter()
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('expenses/summary/', ExpenseSummaryView.as_view(), name='expense-summary'),
    path('', include(router.urls)),
    
]