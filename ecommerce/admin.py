from django.contrib import admin

from ecommerce.models import (
    Brand,
    Product,
    Sell,
    ProductEntry,
    ProductExit,
)


class ProductExitInlines(admin.TabularInline):
    model = ProductExit
    extra = 0


class SellAdmin(admin.ModelAdmin):
    inlines = [ProductExitInlines]


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Sell, SellAdmin)
admin.site.register(ProductEntry)
admin.site.register(ProductExit)
