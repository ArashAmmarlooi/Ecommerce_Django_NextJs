from django.contrib import admin
from Ecommerce.models import (
    Category,
    Product,
    Subcategory,
    Productspecification,
    Productimages,
)


# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    pass


class Subcategoryadmin(admin.ModelAdmin):
    model = Subcategory
    list_display = [
        "name",
        "get_name",
    ]

    def get_name(self, obj):
        return obj.category.name

    get_name.admin_order_field = "category"  # Allows column order sorting
    get_name.short_description = "دسته بندی"  # Renames column head


class Productadmin(admin.ModelAdmin):
    model = Product
    list_display = [
        "name",
        "get_name",
    ]

    def get_name(self, obj):
        return obj.subcategory.name

    get_name.admin_order_field = "subcategory"  # Allows column order sorting
    get_name.short_description = "زیر دسته بندی"  # Renames column head


class Productspecificationadmin(admin.ModelAdmin):
    model = Product
    list_display = [
        "name",
        "get_name",
    ]

    def get_name(self, obj):
        return obj.product.name

    get_name.admin_order_field = "product"  # Allows column order sorting
    get_name.short_description = "محصول"  # Renames column head


admin.site.register(Category, Categoryadmin)
admin.site.register(Subcategory, Subcategoryadmin)
admin.site.register(Product, Productadmin)
admin.site.register(Productspecification, Productspecificationadmin)
