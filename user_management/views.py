from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test")




class ExpertAPIView(ListCreateAPIView):

    serializer_class = ExpertSerializer
    queryset=EXPERT.objects.all()
    

    def post(self, request):

        expert=EXPERT(firstname="ahmed",lastname="belhajsalah")
        expert.save()

        return Response(request.data)

class ExpertDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset=EXPERT.objects.all()

    def destroy(self, request):
        return Response({"delete": "nothing"})




class AgentAPIView(ListCreateAPIView):

    serializer_class = AgentSerializer
    queryset=AGENT.objects.all()
    

    def post(self, request):
        

        agent=AGENT(firstname = "fedi", lastname = "baccouche",expertid=EXPERT.objects.get(pk=2)
        )
        agent.save()
        return Response(request.data)
        

class AgenttDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AgentSerializer
    queryset=AGENT.objects.all()

    def destroy(self, request):
        return Response({"delete": "nothing"})