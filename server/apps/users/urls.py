from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('teams/', views.TeamsView.as_view(), name='teams'),
    path('teams/<int:pk>/', views.TeamsDetailView.as_view(), name='teams-detail'),
    path('teams/<int:pk>/members/', views.TeamsMembersView.as_view(), name='teams-members'),

    path('api/v1/users/', views.UserListViewSet.as_view(), name='api-user-list'),
    path('api/v1/users/<str:username>/', views.UserDetailViewSet.as_view(), name='api-user-detail'),
    path('api/v1/teams/', views.TeamsViewSet.as_list(), name='api-team-list'),
    path('api/v1/teams/<int:pk>', views.TeamsViewSet.as_detail(), name='api-team-detail'),
]
