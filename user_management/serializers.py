from rest_framework import serializers
from .models import *



class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model=EXPERT
        fields= '__all__'

class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model=AGENT
        fields= '__all__'
