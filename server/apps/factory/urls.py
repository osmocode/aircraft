from django.urls import path
from apps.factory import views

app_name = 'factory'

urlpatterns = [
    path('', views.FactoryView.as_view(), name='index'),
    path('part/<slug:pk>/', views.FactoryPartDetailView.as_view(), name='part-detail'),
    path('model/<slug:pk>/', views.FactoryModelDetailView.as_view(), name='model-detail'),
]
