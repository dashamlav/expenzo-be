from rest_framework import serializers
from functools import reduce

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