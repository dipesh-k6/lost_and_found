from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ItemImage

@receiver(post_delete, sender=ItemImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)