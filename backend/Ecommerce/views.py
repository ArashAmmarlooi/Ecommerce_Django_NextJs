from django.shortcuts import render
from . import models
from .models import Category, Subcategory, Product
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from Ecommerce.serializers import (
    Categoryserializer,
    SubCategoryserializer,
    Productserializer,
    ProductSpecificationserializer,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Q


# Create your views here.


class Categorylist(generics.ListAPIView):
    serializer_class = Categoryserializer

    def get_queryset(self, format=None):
        category = Category.objects.all()
        return category


class SubCategorylist(generics.ListAPIView):
    serializer_class = SubCategoryserializer

    def get_queryset(self, format=None):
        subcategory = Subcategory.objects.all()
        return subcategory


class ProductList(generics.ListAPIView):
    serializer_class = Productserializer
    # serializer_class = ProductSpecificationserializer

    def get_queryset(self, format=None):
        products = Product.objects.all()
        return products
        # serializer = Productserializer(products, many=True)
        # return Response(serializer.data)


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = Productserializer

    def get_queryset(self, format=None):
        queryset = Product.objects.all()
        productcat = queryset.filter(id=self.kwargs["pk"])
        return productcat
        # serializer = Productserializer(products, many=True)
        # return Response(serializer.data)


class ProductsByCategory(generics.ListAPIView):
    serializer_class = Productserializer
    # queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.all()
        discount = self.request.query_params.get("discount")
        in_stock = self.request.query_params.get("in_stock")
        brand = self.request.query_params.getlist("brand")
        params = {}
        productcat = queryset.filter(
            category__in=Category.objects.filter(slug=self.kwargs["slug"])
        )

        if discount is not None:
            params["discount"] = discount
        if in_stock is not None:
            params["in_stock"] = in_stock

        if not params and not brand:
            return productcat
        if params and not brand:
            queryset = productcat.filter(**params)
        if params and brand:
            queryset = productcat.filter(brand__in=brand).filter(**params)
        if not params and brand:
            queryset = productcat.filter(brand__in=brand)
        return queryset


class ProductsBySubCategory(generics.ListAPIView):
    serializer_class = Productserializer

    def get_queryset(self):
        queryset = Product.objects.all()
        discount = self.request.query_params.get("discount")
        in_stock = self.request.query_params.get("in_stock")
        brand = self.request.query_params.getlist("brand")
        params = {}
        productcat = queryset.filter(
            subcategory__in=Subcategory.objects.filter(slug=self.kwargs["subslug"])
        )

        if discount is not None:
            params["discount"] = discount
        if in_stock is not None:
            params["in_stock"] = in_stock

        if not params and not brand:
            return productcat
        if params and not brand:
            queryset = productcat.filter(**params)
        if params and brand:
            queryset = productcat.filter(brand__in=brand).filter(**params)
        if not params and brand:
            queryset = productcat.filter(brand__in=brand)
        return queryset
