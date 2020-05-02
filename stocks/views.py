from django.shortcuts import render

# Create your views here.

from django.urls import reverse
from django.shortcuts import render, HttpResponse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings

def view_that_asks_for_money(request):
    host = request.get_host()
    # What you want the button to do.
    paypal_dict = {
        "cmd": "_xclick-subscriptions",
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "a3": "9.99",  # monthly price
        "p3": 1,  # duration of each unit (depends on unit)
        "t3": "M",  # duration unit ("M for Month")
        "src": "1",  # make payments recur
        "sra": "1",  # reattempt payment on payment error
        "no_note": "1",  # remove extra notes (optional)
        "item_name": "my cool subscription",
        "notify_url": 'https://{}{}'.format(host,reverse('paypal-ipn')),
        "return": 'https://{}{}'.format(host,reverse('success-view')),
        "cancel_return": 'https://{}{}'.format(host,reverse('success-view')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
    context = {"form": form}
    return render(request, "payment.html", context)


def success_view(request):
    return HttpResponse("Success <a href='/'>Homepage</a>")
