import graphene
from django.db.models import F
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
            Product.objects.filter(categories=OuterRef('categories'))
            .filter(shop=OuterRef('shop'))
            .order_by('price')
            .values('price')[:1]
        )

        return Product.objects.annotate(min_price=Subquery(subquery)).filter(price=F('min_price'))


schema = graphene.Schema(query=Query)
