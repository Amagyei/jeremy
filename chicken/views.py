from django.shortcuts import render
from .models import chicken

# Create your views here.

def register_chicken(request, chicken_id):
    if request.method == "POST":
        image = request.FILES["image"]
        chicken_id = request.POST["chicken_id"]
        chicken.objects.create(image=image, chicken_id=chicken_id)
        return render(request, "chicken/register_chicken.html")

    return render(request, "chicken/register_chicken.html")