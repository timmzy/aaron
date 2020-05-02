from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    print(">>> From signal", ipn)
    if ipn.payment_status == 'Completed':
        print('<<<', ipn)
