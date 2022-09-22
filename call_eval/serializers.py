from subprocess import call
from rest_framework import serializers
from .models import *

class businessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusinessUnit
        fields= '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields= '__all__'

class GrilleUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grille
        fields= '__all__'

class CritereSerializer(serializers.ModelSerializer):
    class Meta:
        model=Critere
        fields= '__all__'

class SousCritereSerializer(serializers.ModelSerializer):
    class Meta:
        model=SousCritere
        fields= '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model=Call
        fields= '__all__'

class ReportCallSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReportCall
        fields= '__all__'

class CritereScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=CritereScore
        fields= '__all__'


class SousCritereScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=SousCritereScore
        fields= '__all__'

class AgentSerializer(serializers.ModelSerializer):
    class Meta :
        model=Agent
        fields="__all__"