from django.db import models
from django.contrib.auth.models import AbstractUser
from account.usermanager import CustomUserManager
import random
import string


class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, unique=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=False)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True)
    verification_code = models.CharField(max_length=100, null=True, blank=True)

    def generate_verification_code(self):
        code = "".join(random.choices(string.ascii_letters + string.digits, k=20))
        self.verification_code = code
        self.save()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    def __str__(self):
        return self.email

    # def __unicode__(self):
    #     return "%s" % (self.price)

    def get_absolute_url(self):
        return reverse("store:user", args=[self.slug])
