from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model


# class MyUserManager(BaseUserManager):
#     def create_user(self, mobile, password=None, **other_fields):
#         if not mobile:
#             raise ValueError("شماره همراه را وارد کنید..")
#         user = self.model(mobile=mobile, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, mobile, password=None, **other_fields):
#         other_fields.setdefault("is_staff", True)
#         other_fields.setdefault("is_superuser", True)
#         other_fields.setdefault("is_active", True)

#         if other_fields.get("is_staff") is not True:
#             raise ValueError("Superuser muse have is_staff=True")
#         if other_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser muse have is_superuser=True")
#         return self.create_user(mobile, password, **other_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("ایمیل خود را وارد کنید ... ")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print(user, "user in manager")
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
