from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models

User = get_user_model()
class FactoryNestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class FactoryModelSerializer(serializers.ModelSerializer):
    made_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    made_by = FactoryNestedUserSerializer(read_only=True)

    class Meta:
        model = models.AircraftModelFactory
        fields = '__all__'


class FactoryPartSerializer(serializers.ModelSerializer):
    made_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    made_by = FactoryNestedUserSerializer(read_only=True)

    class Meta:
        model = models.AircraftPartFactory
        fields = '__all__'