from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import Group, Permission
from rest_framework import generics, mixins
from rest_framework.response import Response
from apps.core.mixins import CrudViewSet
from . import serializers

User = get_user_model()
# Create your views here.
class TeamsView(TemplateView):
    template_name = 'teams/teams_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_list'] = Group.objects.all()
        return context
    
class TeamsDetailView(DetailView):
    model = Group
    template_name = 'teams/teams_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_list'] = Permission.objects.all()
        return context

    def delete(self, request, *args, **kwargs):
        print(request.DELETE)
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # TODO
        if 'remove' in request.POST and 'pk' in kwargs:
            Group.objects.get(pk=kwargs['pk']).user_set.remove(request.POST['remove'])
        return super().get(request, *args, **kwargs)


class UserListViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailViewSet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        if kwargs.get(self.lookup_field) == 'me':
            return Response(self.get_serializer(request.user).data)
        return self.retrieve(request, *args, **kwargs)
    
class TeamsViewSet(CrudViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.TeamSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    