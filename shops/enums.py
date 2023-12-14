from django.db import models


class ShopTypes(models.TextChoices):
    SPORT = 'sport', 'Sport'
    FOOD = 'food', 'Food'
    ELECTRONICS = 'electronics', 'Electronics'
