import graphene
from django.db.models import F
from django.db.models import Min
from django.db.models import OuterRef
from django.db.models import Subquery
from graphene_django import DjangoObjectType

from shops.models import Category
from shops.models import Product
from shops.models import Shop


class ShopsType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = '__all__'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class Query(graphene.ObjectType):
    lowest_in_each_category = graphene.List(ProductType)

    def resolve_lowest_in_each_category(self, info, **kwargs):
        subquery = (
            Product.objects.filter(shop_id=OuterRef('shop_id'), categories=OuterRef('categories'))
            .values('shop_id', 'categories')
            .annotate(min_price=Min('price'))
            .values('min_price')
        )

        result = Product.objects.annotate(category_id=F('categories__id'), cheapest_price=Subquery(subquery)).filter(
            price=F('cheapest_price')
        )
        return result


schema = graphene.Schema(query=Query)
