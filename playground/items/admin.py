from django.contrib import admin

from playground.items.models import Item


# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name"]
