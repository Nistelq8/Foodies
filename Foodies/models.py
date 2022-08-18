from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Ingredients(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)   

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ingredient = models.ManyToManyField(Ingredients)
    cat = models.ManyToManyField(Category)
    


