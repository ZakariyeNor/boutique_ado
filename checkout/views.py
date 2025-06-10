from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_from = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_from': order_from,
    }

    return render(request, template, context)