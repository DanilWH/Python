

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Available pizzas page.
    path('pizzas/', views.pizzas, name='pizzas'),

    # Available pizzas toppings page.
    path('pizzas/<int:topings_id>/', views.topings, name='topings')
]