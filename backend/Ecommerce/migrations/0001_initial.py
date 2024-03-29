# Generated by Django 4.2.5 on 2023-12-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_collation="utf8_general_ci",
                        default="",
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name="نام دسته بندی",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_collation="utf8_persian_ci",
                        max_length=200,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to="media/", verbose_name="تصویر"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دسته بندی",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        db_collation="utf8_general_ci",
                        default="",
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("brand", models.CharField(blank=True, max_length=200, null=True)),
                ("image", models.ImageField(null=True, upload_to="media/")),
                (
                    "discription",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "price",
                    models.CharField(
                        blank=True, db_index=True, max_length=50, null=True
                    ),
                ),
                ("discount", models.CharField(blank=True, max_length=2, null=True)),
                (
                    "discount_price",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("count", models.IntegerField(blank=True, max_length=50, null=True)),
                ("in_stock", models.CharField(blank=True, max_length=50, null=True)),
                ("rating", models.IntegerField(blank=True, max_length=50, null=True)),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_collation="utf8_persian_ci",
                        max_length=200,
                        null=True,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ecommerce.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "محصولات",
                "verbose_name_plural": "محصولات",
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_collation="utf8_general_ci",
                        default="",
                        max_length=100,
                        null=True,
                        unique=True,
                    ),
                ),
                ("image", models.ImageField(null=True, upload_to="media/")),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_collation="utf8_persian_ci",
                        max_length=200,
                        null=True,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ecommerce.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "زیر دسته بندی",
                "verbose_name_plural": "زیر دسته بندی",
            },
        ),
        migrations.CreateModel(
            name="Productspecification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                (
                    "introduction",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                (
                    "instruction",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("skintype", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("مردانه", "زنانه"),
                            ("زنانه", "مردانه"),
                            ("هر دو", "هر دو"),
                        ],
                        default="مردانه",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "specification",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "discription",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("age", models.CharField(blank=True, max_length=30, null=True)),
                ("boxtype", models.CharField(blank=True, max_length=30, null=True)),
                ("producttype", models.CharField(blank=True, max_length=30, null=True)),
                ("size", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "performance",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productspecification",
                        to="Ecommerce.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "مشخصات محصول",
                "verbose_name_plural": "مشخصات محصول",
            },
        ),
        migrations.CreateModel(
            name="Productimages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("images", models.ImageField(null=True, upload_to="media/")),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_collation="utf8_persian_ci",
                        max_length=200,
                        null=True,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ecommerce.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "تصاویر محصول",
                "verbose_name_plural": "تصاویر محصول",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Ecommerce.subcategory"
            ),
        ),
    ]
