from django.db import models
from django.contrib.auth.models import User
import datetime
from setuptools.command.alias import alias

class lkpPing(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class lkpResult(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class lkpFrequency(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# note related_name for mult FK lookups    
class Sites(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    url = models.URLField(max_length=500)
    lastCheck = models.DateTimeField(blank=True,null=True)
    ping = models.ForeignKey(lkpPing, on_delete=models.CASCADE)
    lastResult = models.ForeignKey(lkpResult, on_delete=models.CASCADE, related_name='site_last_result', blank=True,null=True)
    desiredResult = models.ForeignKey(lkpResult, on_delete=models.CASCADE, related_name='site_desired_result')
    resultValue = models.CharField(max_length=500,blank=True,null=True)
    frequencyType = models.ForeignKey(lkpFrequency, on_delete=models.CASCADE)
    frequency = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name
