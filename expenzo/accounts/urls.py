from django.urls import path
from .views import LoginView, RegisterView, ValidateTokenView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('validate-token', ValidateTokenView.as_view(), name='validate-token'),
]