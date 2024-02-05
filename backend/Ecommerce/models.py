from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        default="",
        unique=True,
        db_collation="utf8_general_ci",
        verbose_name="نام دسته بندی",
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        null=True,
        db_collation="utf8_persian_ci",
    )
    image = models.ImageField(upload_to="media/", null=True, verbose_name="تصویر")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:Category_list", args=[self.slug])


class Subcategory(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        default="",
        unique=True,
        db_collation="utf8_general_ci",
    )
    image = models.ImageField(upload_to="media/", null=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        null=True,
        db_collation="utf8_persian_ci",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "زیر دسته بندی"
        verbose_name_plural = "زیر دسته بندی"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:Subcategory_list", args=[self.slug])


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        default="",
        unique=True,
        db_collation="utf8_general_ci",
    )
    brand = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="media/", null=True)
    discription = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(db_index=True, max_length=50, blank=True, null=True)
    discount = models.CharField(blank=True, null=True, max_length=2)
    discount_price = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(max_length=50, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        null=True,
        db_collation="utf8_persian_ci",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s" % (self.price)

    def get_absolute_url(self):
        return reverse("store:Product_list", args=[self.slug])


class Productspecification(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
    )
    introduction = models.CharField(max_length=400, blank=True, null=True)
    instruction = models.CharField(max_length=400, blank=True, null=True)
    skintype = models.CharField(max_length=20, blank=True, null=True)
    MEN = "زنانه"
    WOMEN = "مردانه"
    BOTH = "هر دو"
    GENDER = [
        (WOMEN, "زنانه"),
        (MEN, "مردانه"),
        (BOTH, "هر دو"),
    ]
    gender = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=GENDER,
        default=WOMEN,
    )
    country = models.CharField(max_length=20, blank=True, null=True)
    specification = models.CharField(max_length=500, blank=True, null=True)
    discription = models.CharField(max_length=500, blank=True, null=True)
    age = models.CharField(max_length=30, blank=True, null=True)
    boxtype = models.CharField(max_length=30, blank=True, null=True)
    producttype = models.CharField(max_length=30, blank=True, null=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    performance = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(
        Product,
        related_name="productspecification",
        on_delete=models.CASCADE,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مشخصات محصول"
        verbose_name_plural = "مشخصات محصول"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s" % (self.price)

    def get_absolute_url(self):
        return reverse("store:Product_list", args=[self.slug])


class Productimages(models.Model):
    images = models.ImageField(upload_to="media/", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        null=True,
        db_collation="utf8_persian_ci",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تصاویر محصول"
        verbose_name_plural = "تصاویر محصول"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s" % (self.price)

    def get_absolute_url(self):
        return reverse("store:Product_list", args=[self.slug])
