from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from apps.core.mixins import CrudViewSet
from . import serializers, models, forms

# Create your views here.
@login_required
def index(request):
    return render(request, 'production/aircraft_index.html')

class AircraftModelView(TemplateView):
    template_name = 'production/aircraft_model.html'
    model = models.AircraftModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'model_list': self.model.objects.all(),
        }
        return context

class AircraftModelCreateView(CreateView):
    form_class = forms.AircraftModelForm
    success_url = reverse_lazy('production:model')
    template_name = 'production/aircraft_model_create.html'

class AircraftPartView(TemplateView):
    template_name = 'production/aircraft_part.html'
    model = models.AircraftPart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'part_list': self.model.objects.all(),
        }
        return context

class AircraftPartCreateView(CreateView):
    form_class = forms.AircraftPartForm
    success_url = reverse_lazy('production:part')
    template_name = 'production/aircraft_part_create.html'


class AircraftModelViewSet(CrudViewSet):
    serializer_class = serializers.AircraftModelSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    def get_queryset(self):
        return models.AircraftModel.objects.all()

class AircraftPartViewSet(CrudViewSet):
    serializer_class = serializers.AircraftPartSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    def get_queryset(self):
        return models.AircraftPart.objects.all()