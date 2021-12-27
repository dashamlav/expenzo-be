
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from .models import Expense
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class GetAllExpensesView(ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(appUser=user).order_by('-date')
    

class CreateExpenseView(CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(appUser=self.request.user)


class UpdateExpenseView(GenericAPIView, UpdateModelMixin):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def get_object(self):
        filter_kwargs = {
            'appUser': self.request.user,
            'id' : self.request.data.get('id', None)
        }
        print(filter_kwargs)
        return get_object_or_404(Expense, **filter_kwargs)



    
    