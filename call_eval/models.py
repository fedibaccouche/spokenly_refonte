from turtle import ondrag
from django.db import models

# Create your models here.
class BusinessUnit(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Activity(models.Model):

    name = models.CharField(max_length=700,null=False)
    business_unit=models.ForeignKey(BusinessUnit,on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return self.name



class Agent(models.Model):
    name = models.CharField(max_length=50)
    #activity = models.ManyToManyField(Activity)
    nb_callqualification = models.IntegerField(default=0)
    nb_situation_inacceptable = models.IntegerField(default=0)
    activity=models.ForeignKey(Activity,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name

    def __incNumbCallQualification__(self):
        self.nb_callqualification += 1

    def __incNumbSituationInacceptable__(self):
        self.nb_situation_inacceptable += 1


class Grille(models.Model):
    name = models.CharField(max_length=700,null=False)
    activity=models.ManyToManyField(Activity)
    #created_at = models.DateTimeField(auto_now_add=True, help_text='This field represents the date of the revocation of the certificate')
    #updated_at = models.DateTimeField(auto_now_add=False, blank=True, null=True, help_text='This field represents the date of the update of the object')
    #is_used = models.BooleanField(default=False) # field to be reviewed again 

class Critere(models.Model):
    name = models.CharField(max_length=700,null=False)
    grille=models.ManyToManyField(Grille)


class SousCritere(models.Model):

    name = models.CharField(max_length=700,null=False)
    critere=models.ForeignKey(Critere,on_delete=models.SET_NULL,null=True)
    coeff=models.PositiveSmallIntegerField(null=False)
    SI_exits=models.BooleanField(default=False)

class Call(models.Model):
    CALL_TYPE_CHOICES = (
        (1, 'AE'),
        (2, 'AS')
    )

    CALL_STATUS_CHOICES = (
        (0, 'Non évalué'),
        (1, 'En cours'),
        (2, 'Evalué')
    )

    class Meta:
        ordering = ['-date']

    call_type = models.PositiveSmallIntegerField(choices=CALL_TYPE_CHOICES, null=True, blank=True)
    call_status=models.PositiveSmallIntegerField(choices=CALL_STATUS_CHOICES,null=True,blank=True)
    treated = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    grille=models.ForeignKey(Grille,on_delete=models.SET_NULL,null=True)
    agent=models.ForeignKey(Agent,on_delete=models.SET_NULL,null=True)
    


class ReportCall(models.Model):
    call=models.ForeignKey(Call,null=True,on_delete=models.SET_NULL)
    score=models.PositiveIntegerField(default=0)

class CritereScore(models.Model):
    reportcall=models.ForeignKey(ReportCall,null=True,on_delete=models.SET_NULL)
    critere=models.ForeignKey(Critere,null=True,on_delete=models.SET_NULL)
    score=models.PositiveIntegerField(default=0)

class SousCritereScore(models.Model):
    sousCritere=models.ForeignKey(SousCritere,null=True,on_delete=models.SET_NULL)#change do nothing to set null
    criterescore=models.ForeignKey(CritereScore,null=True,on_delete=models.SET_NULL)
    score=models.CharField(max_length=100,null=True)
    #add 4 possible values for score 
