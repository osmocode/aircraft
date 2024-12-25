from django.urls import path
from apps.users import views

app_name = 'users'

urlpatterns = [
    path('teams/', views.TeamsView.as_view(), name='teams'),
    path('teams/<int:pk>/', views.TeamsDetailView.as_view(), name='teams-detail'),
]
