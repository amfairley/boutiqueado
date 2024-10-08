from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Handles signal from post_save events
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


# Handles signal from post_delete events
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
