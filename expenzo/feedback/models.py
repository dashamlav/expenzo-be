from django.db import models


class FeedbackForm(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    feedback = models.TextField(max_length=1000, null=False, blank=False)
