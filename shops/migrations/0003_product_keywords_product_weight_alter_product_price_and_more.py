# Generated by Django 5.0 on 2023-12-15 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shops', '0002_auto_20231214_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.JSONField(
                blank=True,
                default=list,
                help_text='Keywords must be entered using a comma-separated list of keywords. Example: ["keyword1", "keyword2", "keyword3"]',
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='The price of the product in UAH.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sales_commission',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
            ),
        ),
    ]