from django import forms
from django.forms import fields, widgets
from apps.production.models import AircraftModel, AircraftPart

class AircraftModelForm(forms.ModelForm):
    class Meta:
        model = AircraftModel
        fields = '__all__'
        labels = {
            'name': 'Aircraft Type Name',
            'desc': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'classes': 'form-control'}),
            'desc': forms.Textarea(attrs={'classes': 'form-control', 'rows': 3}),
        }

class AircraftPartForm(forms.ModelForm):
    class Meta:
        model = AircraftPart
        fields = '__all__'
        labels = {
            'name': 'Aircraft Part Name',
            'desc': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'classes': 'form-control'}),
            'desc': forms.Textarea(attrs={'classes': 'form-control', 'rows': 3}),
        }


        

