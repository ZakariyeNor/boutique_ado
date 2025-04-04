from django.http import HttpResponse

class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a genric/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled Webhook received> {event["type"]}',
            status=200
        )


    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent_succeeded webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook received> {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent_failed webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook received> {event["type"]}',
            status=200
        )