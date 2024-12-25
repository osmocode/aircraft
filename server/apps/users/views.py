from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import Group, Permission

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
    

