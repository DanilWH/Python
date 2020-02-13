from django.shortcuts import render

def index(request):
    """The home page of the application meal_plans."""
    return render(request, 'meal_plans/index.html')