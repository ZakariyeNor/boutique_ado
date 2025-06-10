from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RYRDwQKoFv6KjtXawTWThKMBvxyiFqAorU'
        'zQFkRZ0ZU6K9EpE80pDY6EZiF1F1MVxJ40DVY648YtS0FlTBWLgGQ00W20IGeq6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

