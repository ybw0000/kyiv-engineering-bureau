# Generated by Django 5.0 on 2023-12-14 20:22

from django.db import migrations

from shops.models import Category
from shops.models import Shop
from shops.models import ShopTypes


def create_initial_data(apps, schema_editor):
    for shop_type in ShopTypes.choices:
        Shop.objects.create(
            name='Example Shop',
            description='Example Shop Description',
            shop_type=shop_type[0],
            latitude=0.0,
            longitude=0.0,
            sales_commission=5.0
        )

    sport_categories = ['Winter', 'Summer', 'Football']
    food_categories = ['Bakery', 'Sweets', 'Alcohol']
    electronics_categories = ['Laptops', 'Smartphones', 'Headphones']

    shop_categories = {
        ShopTypes.SPORT: sport_categories,
        ShopTypes.FOOD: food_categories,
        ShopTypes.ELECTRONICS: electronics_categories
    }

    for shop_type, categories in shop_categories.items():
        for category_name in categories:
            Category.objects.create(name=category_name, shop_type=shop_type)


class Migration(migrations.Migration):
    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]