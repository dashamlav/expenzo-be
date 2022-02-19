import random
from rest_framework import serializers
from functools import reduce
from rest_framework.authentication import TokenAuthentication
from accounts.models import AuthToken
from rest_framework import exceptions

class ExpiringTokenAuthentication(TokenAuthentication):
    model = AuthToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        if token.isExpired:
            raise exceptions.AuthenticationFailed('Token expired')

        return (token.user, token)


class ArrayField(serializers.Field):
    '''
    A custom Serializer Field which can be used to convert a string representation of an array to a python list.
    '''
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError("Input type must be string")
        return data.split(",")


def aggregateToDict(iterable):
    '''
    Converts a list of dictionaries into a single dictionary
    '''
    return reduce(
        lambda initial,value: initial.update(value) or initial,
        iterable,
        {}
    )

def generateOTP():
    return int(random.uniform(0.1,1)*1000000)
