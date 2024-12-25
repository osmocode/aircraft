from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from apps.production.models import AircraftModel, AircraftPart
from .models import AircraftPartFactory, AircraftModelFactory

# Create your views here.
class FactoryView(TemplateView):
    template_name = 'factory/factory_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_factory'] = AircraftModel.objects.all()
        context['part_factory'] = AircraftPart.objects.all()
        return context

class FactoryPartDetailView(DetailView):
    model = AircraftPart
    template_name = 'factory/factory_part.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_list'] = AircraftPartFactory.objects.filter(part_type=self.object).order_by('-made_at')
        context['model_list'] = AircraftModel.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        # TODO handle errors
        if 'model' in request.POST and 'pk' in kwargs:
            AircraftPartFactory.objects.create(
                part_type=AircraftPart.objects.get(pk=kwargs['pk']),
                part_of=AircraftModel.objects.get(pk=request.POST['model']),
                made_by=request.user
            )
        return self.get(request, *args, **kwargs)



class FactoryModelDetailView(DetailView):
    model = AircraftModel
    template_name = 'factory/factory_model.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_list'] = AircraftPart.objects.all()
        context['model_list'] = AircraftModelFactory.objects.filter(model_type=self.object).order_by('-made_at')
        return context
    