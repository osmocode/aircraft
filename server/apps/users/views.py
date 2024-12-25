from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
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
    
    def post(self, request, *args, **kwargs):
        # TODO
        if 'remove' in request.POST and 'pk' in kwargs:
            Group.objects.get(pk=kwargs['pk']).user_set.remove(request.POST['remove'])
        return super().get(request, *args, **kwargs)

class TeamsMembersView(DetailView):
    model = Group
    template_name = 'teams/teams_add_member.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Not sure don't now why
        context['user_list'] = User.objects.all().exclude(groups__pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        if 'add_users' in request.POST and 'pk' in kwargs:
            group = Group.objects.get(pk=kwargs['pk'])
            for user in request.POST.getlist('add_users'):
                try:
                    new_member = User.objects.get(pk=user)
                    group.user_set.add(new_member)
                except Exception as e:
                    print(e)
        return super().get(request, *args, **kwargs)


class UserListViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'last_name', 'first_name', 'email']
    ordering_fields = ['username']
    ordering = ['username']

    def get(self, request, *args, **kwargs):
        if 'no_page' in self.request.query_params:
            self.pagination_class = None
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

    