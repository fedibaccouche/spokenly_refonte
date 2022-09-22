from django.urls import path

from .views import *

urlpatterns = [
    
    path('expert/', ExpertAPIView.as_view(),name="userexpert"),
    path('expert/<int:id>', ExpertDetailsAPIView.as_view(),name="userexpert"),

    path('agent/', AgentAPIView.as_view(),name="useragent"),
    path('agent/<int:id>', AgenttDetailsAPIView.as_view(),name="useragent"),
]