from django.contrib import admin
from .models import *


@admin.register(Food)
class Food(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass
