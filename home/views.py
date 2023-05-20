from django.shortcuts import render, get_object_or_404

from menu.models import MenuItem

# Create your views here.


def index(request):
    """ A view to return the index page """
    template = 'home/index.html'
    
    featured_pizzas = []

    for number in range(1, 5):
        featured_pizzas.append(get_object_or_404(MenuItem, pk=number))

    context = {
        'featured_pizzas': featured_pizzas,
    }

    return render(request, template, context)
