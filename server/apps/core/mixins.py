from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, exceptions, viewsets

# Create your views here.
class CrudViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)

        # Override get_queryset to cache the result
        old_get_queryset = self.get_queryset

        def get_queryset():
            if not hasattr(self, '__get_queryset__'):
                self.__get_queryset__ = old_get_queryset()
            return self.__get_queryset__
        setattr(self, 'get_queryset', get_queryset)


        # Override get_object to cache the result
        old_get_object = self.get_object

        def get_object():
            try:
                if not hasattr(self, '__get_object__'):
                    self.__get_object__ = old_get_object()
                self.check_object_permissions(request, self.__get_object__)
                return self.__get_object__
            except ObjectDoesNotExist:
                raise exceptions.NotFound()
        setattr(self, 'get_object', get_object)

        return request

    def list(self, request, *args, **kwargs):
        if 'no_page' in self.request.query_params:
            self.pagination_class = None
        return super().list(request, *args, **kwargs)

    @classmethod
    def as_list(cls):
        return cls.as_view({'get': 'list', 'post': 'create'})

    @classmethod
    def as_detail(cls):
        return cls.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})