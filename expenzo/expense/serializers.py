from rest_framework import serializers
from .models import Expense

class ListExpenseSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category_string', read_only=False)
    transactionType = serializers.SerializerMethodField('get_transactionType_string', read_only=False)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'category', 'currency', 'description', 'receiptImage', 'transactionType']

    def get_category_string(self, obj):
        return obj.get_category_display()
    
    def get_transactionType_string(self, obj):
        return obj.get_transactionType_display()


class CreateOrUpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'category', 'currency', 'description', 'receiptImage', 'transactionType']
