from django.contrib import admin
from .models import Expense, Collection
# Register your models here.

admin.site.register([Expense, Collection])