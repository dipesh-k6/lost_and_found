from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import ItemImage

@receiver(post_delete, sender=ItemImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

@receiver(pre_save, sender=ItemImage)
def edit_image(sender, instance, **kwargs):
    if instance.pk:
        old = ItemImage.objects.filter(pk=instance.pk).first()

        if old and old.image and old.image != instance.image:
            old.image.delete(save=False)