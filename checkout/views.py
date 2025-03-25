from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag aat the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R6WqAPGNpVOLTSm4kGD433Fd3rT3JH1ni9ZqjOgYkeAPCCogezZU8gt2SrLAGmB0ReKaCRLX5pglwDqSb5vyng200akrDHl1b',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)