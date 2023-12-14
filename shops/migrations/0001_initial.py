# Generated by Django 5.0 on 2023-12-14 20:19

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models
from django.db.migrations import swappable_dependency


class Migration(migrations.Migration):
    initial = True

    dependencies = [swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                (
                    'shop_type',
                    models.CharField(
                        choices=[('sport', 'Sport'), ('food', 'Food'), ('electronics', 'Electronics')], max_length=20
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                (
                    'shop_type',
                    models.CharField(
                        choices=[('sport', 'Sport'), ('food', 'Food'), ('electronics', 'Electronics')], max_length=20
                    ),
                ),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    'sales_commission',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_photos/')),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shops.product'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', through='shops.ProductCategory', to='shops.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shops.shop'
            ),
        ),
        migrations.AddConstraint(
            model_name='productcategory',
            constraint=models.UniqueConstraint(fields=('product', 'category'), name='unique_product_category'),
        ),
    ]
