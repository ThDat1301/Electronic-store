from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Product, User


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "active", "category"]
    search_fields = ["name", "category__name"]
    readonly_fields = ["image_product"]

    def image_product(self, product):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width=160px />".
                         format(img_url=product.image.name, alt=product.name))


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
