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
    model_parts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.AircraftModelFactory
        fields = ('id', 'made_at', 'made_by', 'model_type', 'model_parts')
    
    def get_model_parts(self, value: models.AircraftModelFactory):
        parts = models.AircraftPartFactory.objects.filter(used_by=value)
        return FactoryPartSerializer(parts, many=True).data

class FactoryPartSerializer(serializers.ModelSerializer):
    made_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    made_by = FactoryNestedUserSerializer(read_only=True)
    is_available = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.AircraftPartFactory
        fields = '__all__'
    