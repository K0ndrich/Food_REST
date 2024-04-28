from django.shortcuts import render
from .serializers import FoodSerializer , CategorySerializer
from rest_framework import viewsets

def list_product(request):
    foods = Food.objects.all().order_by("-id")
    context = {"foods": foods}

    return render(request, "product_list/index.html", context)


# -----   API   -------------------------------------------------------------------------------------------------------------------------------------------------

class CategoryAPIView(viewsets.Mode)
    