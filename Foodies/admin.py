from django.contrib import admin

from Foodies import models

to_register = [models.Category, models.Ingredients, models.Recipe]

admin.site.register(to_register)