from dataclasses import fields
from django import forms
from django.contrib.auth import get_user_model
from Foodies import models

User = get_user_model()


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
        
class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    
    
    
class Create_Recipe(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ["title","description","image",]
        
        # widgets = {'Ingredients' : forms.CheckboxSelectMultiple()}
        
        
# class Create_Ingredient(forms.ModelForm):
#     class Meta:
#         model = models.Ingredients
#         fields = ["title","image","category"]
        
# class Create_Category(forms.ModelForm):
#     class Meta:
#         model = models.Category
#         fields = ["title","image"]