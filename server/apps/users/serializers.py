from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from rest_framework.reverse import reverse
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

User = get_user_model()

class NestedPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'url', 'username',
            'email', 'first_name', 'last_name',
            'is_staff', 'is_active', 'date_joined',
            'groups', 'user_permissions')

    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, value):
        request = self.context['request']
        return reverse(
            'users:api-user-detail',
            request=request,
            kwargs={'username': value.username}
        )

class TeamSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    #permissions = NestedPermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'permissions', 'user_set')
    
    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, value):
        request = self.context['request']
        return reverse(
            'users:api-team-detail',
            request=request,
            kwargs={'pk': value.pk}
        )
    