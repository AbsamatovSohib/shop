from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from .models import Card

@receiver(post_save, sender=Card)
def update_card_total_and_promo_code(sender, instance, **kwargs):
    total_price = instance.payment_items.aggregate(total_price=Sum('price'))['total_price'] or 0
    instance.total = total_price
    instance.save(update_fields=['total'])

    if instance.promo_code and instance.total > instance.promo_code.min_bought_price:
        if instance.promo_code.total_usage > 0:
            instance.promo_code.total_usage -= 1
            instance.promo_code.save()
        else:
            instance.promo_code = None
            instance.save(update_fields=['promo_code'])
