from django.urls import path

from .views import *

urlpatterns = [
    
    path('bu/', BusinessUnitAPIView.as_view(),name="userexpert"),
    path('bu/<int:id>', BusinessUnitDetailsAPIView.as_view(),name="userexpert"),
    #path('score/', SousCritereScoreAPIView.as_view(),name="test_score"),
    path('grille/', GrilleAPIView.as_view(),name="test_grille"),
    path('critere/', CritereAPIView.as_view(),name="test_critere"),
    path('sous-critere/', SousCritereScoreAPIView.as_view(),name="test_sous_critere"),
    path("dashbord/",ReportCalls.as_view(),name="dashbord"),
    path("agent/",AgentAPIView.as_view(),name="agent"),
    path("call/",CallAPIView.as_view(),name="call")
]