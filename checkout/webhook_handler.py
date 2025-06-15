from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, request):
        """
        Handle the payment that being succefully completed or
        payment_intent.succeeded webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
    

    def handle_payment_intent_payment_failed(self, request):
        """
        Handle the payment that being failed completed or
        payment_intent.failed webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )