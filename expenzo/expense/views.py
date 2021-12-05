
from rest_framework.generics import ListAPIView
from .models import Expense
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from rest_framework.pagination import PageNumberPagination


class GetAllExpensesView(ListAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(appUser=user)