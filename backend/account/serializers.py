from rest_framework import serializers

from account.models import User


# class UserSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "password", "password2"]

#     def create(self, validated_attrs):
#         # password1 = validated_attrs.get("password")
#         # password2 = validated_attrs.get("password2")

#         # if password1 != password2:
#         #     raise serializers.ValidationError("Passwords do not match.")

#         user = User.objects.create_user(**validated_attrs)
#         print(validated_attrs, "validate attrs in serializer")
#         print(user, "user")
#         return user


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_two = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        password_two = data.get("password_two")
        email_check = User.objects.filter(email=email)

        if password != password_two:
            raise serializers.ValidationError("...رمز عبور هم خوانی ندارد")
        if email_check.exists():
            raise serializers.ValidationError("... این ایمیل قبلا ثبت شده است")
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email is None:
            raise serializers.ValidationError("لطفا ایمیل خود را وارد کنید")
        if password is None:
            raise serializers.ValidationError("لطفا رمز عبور خود را وارد کنید")
        return data
