from django.db import models

# Create your models here.
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received


def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    print(">>> From Model", ipn_obj)


valid_ipn_received.connect(show_me_the_money)

