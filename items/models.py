from django.db import models
from utility.common_models import DateTimeModel
from django.conf import settings

class Category(DateTimeModel):
    """model for category"""
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Item(DateTimeModel):
    """model for item"""
    ITEM_TYPES = [
        ("lost", "Lost"),
        ("found", "Found")
    ]

    ITEM_STATUS = [
        ("active", "Active"),
        ("resolved", "Resolved"),
        ("cancelled", "Cancelled")
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=50)
    type = models.CharField(choices=ITEM_TYPES, max_length=12)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="items")
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    specific_location = models.CharField(max_length=150, blank=True)
    date = models.DateField()
    status = models.CharField(choices=ITEM_STATUS, default="active", max_length=12)

    # class Meta:
    #     db_table = "Items"
    #     ordering = "id"

    def __str__(self):
        return self.title

class ItemImage(DateTimeModel):
    """model for item image"""
    image = models.ImageField(upload_to='item_images/')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.item.title

