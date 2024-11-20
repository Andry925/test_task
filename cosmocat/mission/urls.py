from django.urls import path

from . import views

urlpatterns = [
    path('missions', views.MissionListView.as_view(), name='mission-create'),
    path('missions/<int:pk>', views.MissionDetailView.as_view(), name='mission-detail'),
]
