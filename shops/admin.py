from django.contrib import admin

from shops.models import Category
from shops.models import Photo
from shops.models import Product
from shops.models import ProductCategory
from shops.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory


class ProductPhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductCategoryInline,
        ProductPhotoInline,
    ]
    exclude = ('categories',)
