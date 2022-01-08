from django.urls import path
from .views import GetAllExpensesView, CreateExpenseView, UpdateOrDeleteExpenseView

urlpatterns = [
    path('get-expenses', GetAllExpensesView.as_view(), name='get-expenses'),
    path('create-expense', CreateExpenseView.as_view(), name='create-expense'),
    path('update-expense', UpdateOrDeleteExpenseView.as_view(), name='update-expense'),
]