from django.contrib import admin
from . import models

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "type", "status", "date"]
    list_editable = ["category"]
    search_fields = ["title", "description", "specific_location", "district", "city"]
    list_filter = ["created_at", "city", "category"]
    list_per_page = 10

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 15
