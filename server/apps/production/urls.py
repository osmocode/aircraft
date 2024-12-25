from django.urls import path
from apps.production import views

app_name = 'production'

urlpatterns = [
    path('production/', views.index, name='index'),
    path('production/model/', views.AircraftModelView.as_view(), name='model'),
    path('production/model/create', views.AircraftModelCreateView.as_view(), name='model-create'),
    path('production/part/', views.AircraftPartView.as_view(), name='part'),
    path('production/part/create', views.AircraftPartCreateView.as_view(), name='part-create'),

    path('api/v1/production/model/', views.AircraftModelViewSet.as_list(), name='api-prod-model-list'),
    path('api/v1/production/model/<str:name>', views.AircraftModelViewSet.as_detail(), name='api-prod-model-detail'),
    path('api/v1/production/part/', views.AircraftPartViewSet.as_list(), name='api-prod-part-list'),
    path('api/v1/production/part/<str:name>', views.AircraftPartViewSet.as_detail(), name='api-prod-part-detail'),
]
