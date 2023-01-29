from django.contrib import admin
# Register your models here.
from .models import Shop_data


@admin.register(Shop_data)


class Shop_dataAdmin(admin.ModelAdmin):
    list_display=('id', 'name','brand','slug','price')
