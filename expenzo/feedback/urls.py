from django.urls import path
from .views import PostFeedBack

urlpatterns = [
    path('post-feedback', PostFeedBack.as_view(), name='post-feedbacks'),
]