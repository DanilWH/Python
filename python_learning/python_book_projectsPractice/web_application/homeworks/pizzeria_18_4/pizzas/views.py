from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def topings(request, topings_id):
    pizza = Pizza.objects.get(id=topings_id)
    topings = pizza.toping_set.all()
    context = {'pizza': pizza, 'topings': topings}
    return render(request, 'pizzas/topings.html', context)