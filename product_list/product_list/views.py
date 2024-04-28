from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


def list_product(request):
    foods = Food.objects.all().order_by("-id")
    context = {"foods": foods}

    return render(request, "product_list/index.html", context)


# -----   API   -------------------------------------------------------------------------------------------------------------------------------------------------


class FoodAPIView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # можно ограничить типы методов с какими может взаемодействовать сериалайзер
    http_method_names = ["get"]


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get"]
