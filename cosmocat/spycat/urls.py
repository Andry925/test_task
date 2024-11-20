from django.urls import path

from . import views

urlpatterns = [
    path('cats', views.SpycatListCreateView.as_view(), name='spycat'),
    path('cat-update/<int:pk>', views.SpycatUpdateView.as_view(), name='spycat-update'),
    path('cat-delete/<int:pk>', views.SpycatRetrieveDestroyView.as_view(), name='spycat-delete'),
]
