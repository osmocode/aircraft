from django.urls import path
from apps.factory import views

app_name = 'factory'

urlpatterns = [
    path('factory/', views.FactoryView.as_view(), name='index'),
    path('factory/part/<slug:pk>/', views.FactoryPartDetailView.as_view(), name='part-detail'),
    path('factory/model/<slug:pk>/', views.FactoryModelDetailView.as_view(), name='model-detail'),

    path('api/v1/factory/model/', views.FactoryModelViewSet.as_list(), name='api-factory-model-list'),
    path('api/v1/factory/model/<slug:name>/', views.FactoryModelViewSet.as_detail(), name='api-factory-model-detail'),
    path('api/v1/factory/part/', views.FactoryPartViewSet.as_list(), name='api-factory-part-list'),
    path('api/v1/factory/part/<slug:name>/', views.FactoryPartViewSet.as_detail(), name='api-factory-part-detail'),

]
