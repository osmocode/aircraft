from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/register.html'

@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('users:api-user-list', request=request, format=format),
        'teams': reverse('users:api-team-list', request=request, format=format),
        'production-model': reverse('production:api-prod-model-list', request=request, format=format),
        'production-part': reverse('production:api-prod-part-list', request=request, format=format),
        'factory-model': reverse('factory:api-factory-model-list', request=request, format=format),
        'factory-part': reverse('factory:api-factory-part-list', request=request, format=format),
    })