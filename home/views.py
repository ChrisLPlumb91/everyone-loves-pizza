from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomerMessage
from .forms import CustomerMessageForm
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


@login_required
def customer_contact(request):
    """
    A view to return the contact us page, and to enable the submission
    of messages by users.
    """
    template = 'home/contact_us.html'

    if request.method == 'POST':
        form = CustomerMessageForm(request.POST)

        if form.is_valid():
            user_message = form.save(commit=False)
            user_message.customer = request.user
            user_message.save()

            messages.success(request, 'Thank you for your message. '
                             'A member of staff will reply to you via '
                             'email in the next 1-2 working days.')
        else:
            messages.error(request, 'Error: Message not sent.')

    form = CustomerMessageForm()

    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, template, context)
