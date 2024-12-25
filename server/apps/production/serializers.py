from rest_framework import serializers
from rest_framework.reverse import reverse
from . import models
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

class AircraftModelSerializer(serializers.ModelSerializer):
    name = serializers.SlugField(max_length=50, allow_blank=False)
    desc = serializers.CharField(max_length=300, allow_blank=True, default='')
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.AircraftModel
        fields = '__all__'
    
    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, value: models.AircraftModel):
        request = self.context.get('request')
        return reverse(
            'production:api-prod-model-detail',
            request=request,
            kwargs={'name': value.pk}
        )

class AircraftPartSerializer(serializers.ModelSerializer):
    name = serializers.SlugField(max_length=50, allow_blank=False)
    desc = serializers.CharField(max_length=300, allow_blank=True, default='')
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.AircraftPart
        fields = '__all__'
    
    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, value: models.AircraftPart):
        request = self.context.get('request')
        return reverse(
            'production:api-prod-part-detail',
            request=request,
            kwargs={'name': value.pk}
        )