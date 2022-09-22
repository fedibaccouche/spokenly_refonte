from djongo import models

# Create your models here.
class EXPERT(models.Model):
    firstname = models.CharField(max_length=700)
    lastname = models.CharField(max_length=700000,null=True)
    
class AGENT(models.Model):
    firstname = models.CharField(max_length=700) 
    lastname = models.CharField(max_length=700) 
    expertid = models.ForeignKey('EXPERT', on_delete=models.CASCADE)



