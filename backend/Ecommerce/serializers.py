from rest_framework import serializers
from .models import Category, Subcategory, Product


class Categoryserializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        required=False, max_length=None, allow_empty_file=True, use_url=True
    )

    class Meta:
        model = Category
        fields = ["id", "name", "image", "slug"]


class SubCategoryserializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True)
    image = serializers.ImageField(
        required=False, max_length=None, allow_empty_file=True, use_url=True
    )

    class Meta:
        model = Subcategory
        fields = ["id", "name", "category", "image", "slug", "category_id"]


class ProductSpecificationserializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=True, read_only=True)
    # productspecification = ProductSpecificationserializer(many=True, read_only=True)
    # product = serializers.PrimaryKeyRelatedField(
    #     queryset=Product.objects.all(), many=False
    # )

    class Meta:
        model = Product
        fields = "__all__"
        # depth = 1


class Productserializer(serializers.ModelSerializer):
    # productspecification = serializers.ProductSpecificationserializer
    # productspecification = ProductSpecificationserializer(read_only=True, many=True)
    # productspecification = serializers.StringRelatedField(many=True)
    # productspecification = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # productspecification = ProductSpecificationserializer(read_only=True)
    subcategory = serializers.CharField(read_only=True)
    image = serializers.ImageField(
        required=False, max_length=None, allow_empty_file=True, use_url=True
    )
    category = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "brand",
            "image",
            "discription",
            "price",
            "discount",
            "discount_price",
            "count",
            "in_stock",
            "rating",
            "slug",
            "subcategory",
            "category",
            "productspecification",
        ]
        depth = 1
