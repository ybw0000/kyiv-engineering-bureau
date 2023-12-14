from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from shops.enums import ShopTypes


class Shop(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    shop_type = models.CharField(max_length=20, choices=ShopTypes.choices)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    sales_commission = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'{self.id} | {self.name} | {self.get_shop_type_display()}'


class Category(models.Model):
    name = models.CharField(max_length=120)
    shop_type = models.CharField(max_length=20, choices=ShopTypes.choices)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name} | {self.get_shop_type_display()}"


class ProductCategory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'category'],
                name='unique_product_category',
            )
        ]

    def clean(self):
        if self.product.shop.shop_type != self.category.shop_type:
            raise ValidationError("Category doesn't belong to the same shop type as the product.")


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    categories = models.ManyToManyField(Category, related_name='products', through=ProductCategory)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'ID:{self.id} | NAME:{self.name} | SHOP:{self.shop} | PRICE:{self.price}'


class Photo(models.Model):
    image = models.ImageField(upload_to='product_photos/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.image.name
