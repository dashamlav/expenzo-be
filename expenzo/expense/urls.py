from django.urls import path
from .views import GetAllExpensesView

urlpatterns = [
    path('get-expenses', GetAllExpensesView.as_view(), name='get-expenses')
]