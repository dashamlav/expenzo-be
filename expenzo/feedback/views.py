from django.http import HttpResponse
from .models import FeedbackForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class PostFeedBack(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email', None)
        feedback = request.POST.get('feedback')

        FeedbackForm.objects.create(
            name=name,
            email=email,
            feedback=feedback
        )

        return HttpResponse(status=200, content="Feedback stored successfully")
