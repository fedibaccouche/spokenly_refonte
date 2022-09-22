from audioop import avg
from operator import imod
from telnetlib import STATUS
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Avg
import random

# Create your views here.
class BusinessUnitAPIView(ListCreateAPIView):

    serializer_class = businessUnitSerializer
    queryset=BusinessUnit.objects.all()
    

    def post(self, request):

        bu=BusinessUnit(name=request.data["name"])
        bu.save()

        return Response(request.data)

class BusinessUnitDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = businessUnitSerializer
    queryset=BusinessUnit.objects.all()

    def destroy(self, request):
        return Response({"delete": "nothing"})
        

class GrilleAPIView(ListCreateAPIView):

    serializer_class = GrilleUnitSerializer
    queryset=Grille.objects.all()
    

    def post(self, request):

        grille=Grille(name="test grille 2 ")
        grille.save()

        return Response(request.data)


class CritereAPIView(ListCreateAPIView):

    serializer_class = CritereSerializer
    queryset=Critere.objects.all()
    

    def post(self, request):

        critere=Critere(name=request.data["name"])
        gr=Grille.objects.get(id=request.data["grille"])
        critere.save()
        critere.grille.add(gr)

        

        return Response(request.data)

class AgentAPIView(ListCreateAPIView):
    serializer_class=AgentSerializer
    queryset=Agent.objects.all()

    def post(self,request):
        
        for i in range(3,25):
            agent=Agent(id=i,name="agent "+str(i),activity_id=random.randint(1,6))
            agent.save()
        
        return Response("sucess")

class CallAPIView(ListCreateAPIView):
    serializer_class=CallSerializer
    queryset=Call.objects.all()

    def post(self,request):
        
        for i in range(3,5000):
            call=Call(id=i,call_type=1,call_status=0,grille_id=1,agent_id=random.randint(1,24))
            call.save()
        
        return Response("sucess")














class SousCritereScoreAPIView(ListCreateAPIView):
    serializer_class=SousCritereScoreSerializer
    queryset=SousCritere.objects.all()

    def post(self,request):
        # criteres=dict(request.data)
        # for critere in criteres.keys():
        #     souscriteres=criteres.get(critere)
        #     for souscritere in souscriteres.keys():
        #         print(souscriteres[souscritere])
        answers=[0,1,"NE","SI"]
        for i in range(2,5000):
            call_score=0
            report=request.data["report"]
            criteres=report.keys()
            call_id=i              # rollback to request.data["call"] 
            number_cr=0
            list_cr_score=[]
            failed_call=False
            
            

            for critere in criteres:
                
                souscriteres=report[critere]
                total_coef=0
                l=[]
                critere_score=0
                for souscritere in souscriteres:
                    #SI_index=False
                    NE_index=False
                    nom,coef,valeur=souscritere["name"],int(souscritere["coef"]),answers[random.randint(0,2)]# rollback !!souscritere["value"]
                    print("****************\n",coef)
                    print("*****************\n",valeur)
                    print("****************\n",nom)
                    sc=SousCritere.objects.get(name=nom)
                    
                    if valeur =="NE":
                        score=0
                        NE_index=True
                    elif valeur=="SI":
                        score=0
                        failed_call=True
                        #SI_index=True
                    else :
                        score=int(valeur)*coef
                        print("****************\n",score)
                    

                    sc_score=SousCritereScore(score=valeur,sousCritere=sc) 
                    sc_score.save()
                    
                    print("*****************\n",sc)
                    #sc_score.sousCritere.add()
                    # this section has to be modified in order to add SI and NE as possible values
                    l.append(sc_score)
                

                    critere_score+=score
                    print("critere score : \n",critere_score)

                    if not NE_index:
                        total_coef +=coef

                c=Critere.objects.get(name=critere)
                if total_coef!=0:


                    cr_score=critere_score/total_coef * 100
                    print("****************\n",cr_score)
                    print("****************\n",total_coef)
                    print("****************\n",critere_score)
                else:

                    cr_score=critere_score
                    print("****************\n",cr_score)

                criterescore=CritereScore(score=cr_score,critere=c)
                criterescore.save()
                list_cr_score.append(criterescore)
                #criterescore.add(c)
                for i in l :
                    #i.criterescore.add(criterescore)
                    i.criterescore=criterescore
                    i.save()

                call_score+=cr_score
                number_cr+=1

            call=Call.objects.get(id=call_id)

            score_total=call_score/number_cr
            if failed_call :
                score_total=0
            reportcall=ReportCall(score=score_total,call=call)
            reportcall.save()

            for i in list_cr_score:
                i.reportcall=reportcall
                i.save()
            
            call.treated=True
            call.save()
            #reportcall.add(call)
            try :
                agent=Agent.objects.get(id=call.agent_id)
            except Agent.DoesNotExist:
                return HttpResponse(status=502)
            
            if failed_call :
                agent.__incNumbSituationInacceptable__() 

            agent.__incNumbCallQualification__()
            #add agent.save()





            

            




        

        return  Response(
            {"call score" : score_total}
        )
                
class ReportCalls(ListCreateAPIView):
    serialize_class=CallSerializer
    queryset=Call.objects.all()

    def post(self,request):
        report_critere={}
        report_sousCritere={}
        report_agent={}


        average_score=ReportCall.objects.aggregate(Avg("score"))
        # for i,report in enumerate(ReportCall.objects.filter()):
        #     average_score+=report.score/(i+1)

        # for i,critere_sc in enumerate(CritereScore.objects.filter()):
        #     if critere_sc.critere_id !=None  :
                
        #         cr=Critere.objects.get(id=critere_sc.critere_id)
        #         name=cr.name
        #         #report_critere[name]+=critere_sc.score/(i+1)
        #         if report_critere.get(name,True):

        #             report_critere[name]=critere_sc.score

        #         if report_critere.get(name+"number",True):

        #             report_critere[name+"number"]=1

                  
        #         report_critere[name]+=critere_sc.score/report_critere[name+"number"]
        #         report_critere[name+"number"]+=1  
                # for i,report in enumerate(ReportCall.objects.filter()):
        #     average_score+=report.score/(i+1)

        for critere in Critere.objects.filter():
            criteres= CritereScore.objects.filter(critere_id=critere.id)
            name=critere.name
                # if report_critere.get(name,True):
                #      report_critere[name]=critere_score.score
                # report_critere[name]+=critere_score.score/(i+1)
            report_critere[name]=criteres.aggregate(Avg("score"))


        for souscritere in SousCritere.objects.filter():
            souscriteres= CritereScore.objects.filter(critere_id=critere.id)
            name=souscritere.name
            report_sousCritere[name]=souscriteres.aggregate(Avg("score"))
                

            

 
                
        for agent in Agent.objects.filter():
            agent_name=agent.name
            calls=Call.objects.filter(agent_id=agent.id)
            for call in calls : 
                report_byAgent=ReportCall.objects.filter(call_id=call.id)
                score=report_byAgent.aggregate(Avg("score"))
                report_agent[agent_name]={"nom de l'agent":agent.name,"average score":score,"nombre des SI":agent.nb_situation_inacceptable,"nombre des appels :":agent.nb_callqualification}



            
        
        # for i,sc_score in enumerate(SousCritereScore.objects.filter()):
        #     sc=SousCritere.objects.get(id=sc_score.sousCritere_id)
        #     name=sc.name
        #     score=sc_score.score
        #     if sc_score.score=='NE' or sc_score.score=='SI':
        #         score=0
            
        #     if report_sousCritere.get(name,True):
        #         report_sousCritere[name]=int(score)
        #     report_sousCritere[name]+=int(score)/(i+1)
        
        result={}
        
        result["average score"]=average_score
        result["rapport par critere :"]=report_critere
        result["rapport par sous-critere :"]=report_sousCritere
        result["Agents:"]=report_agent

        return Response(
            {"statistiques":result}
        )




            

