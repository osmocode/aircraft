from django.urls import path
from apps.production import views

app_name = 'production'

urlpatterns = [
    path('', views.index, name='index'),
    path('model/', views.AircraftModelView.as_view(), name='model'),
    path('model/create', views.AircraftModelCreateView.as_view(), name='model-create'),
    path('part/', views.AircraftPartView.as_view(), name='part'),
    path('part/create', views.AircraftPartCreateView.as_view(), name='part-create'),
]
