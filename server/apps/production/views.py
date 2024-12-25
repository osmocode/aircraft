from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import AircraftModel, AircraftPart
from .forms import AircraftModelForm, AircraftPartForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'production/aircraft_index.html')

class AircraftModelView(TemplateView):
    template_name = 'production/aircraft_model.html'
    model = AircraftModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'model_list': self.model.objects.all(),
        }
        return context

class AircraftModelCreateView(CreateView):
    form_class = AircraftModelForm
    success_url = reverse_lazy('production:model')
    template_name = 'production/aircraft_model_create.html'

class AircraftPartView(TemplateView):
    template_name = 'production/aircraft_part.html'
    model = AircraftPart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'part_list': self.model.objects.all(),
        }
        return context

class AircraftPartCreateView(CreateView):
    form_class = AircraftPartForm
    success_url = reverse_lazy('production:part')
    template_name = 'production/aircraft_part_create.html'