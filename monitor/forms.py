from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username:")
    password = forms.CharField(label="Password:",widget=forms.PasswordInput)
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]
        
class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Sites
        fields = ["name","description","ping","url","desiredResult","resultValue","frequencyType","frequency"]
        labels = {
            "name": "Site Name",
            "description": "Description",
            "url": "Test URL",
            "ping": "Ping Type",
            "desiredResult": "Desired Type",
            "resultValue": "Desired Value",
            "frequencyType": "Time Period",
            "frequency": "Time Amount",
        }
        widgets = {
            "name": forms.TextInput(attrs={'size': '80', 'class':'inputText'}),
            "frequency": forms.NumberInput(),
            "url": forms.URLInput(),
            "resultValue": forms.TextInput(attrs={'size': '80', 'class':'inputText'}),
            "description": forms.Textarea(attrs={'cols': 80, 'class':'inputText','rows':3})
                   }