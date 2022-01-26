from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    otp = serializers.IntegerField(required=True)
