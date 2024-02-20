from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import authenticate
from rest_framework import status

# from account.renderers import UserRenderer
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
# class CreateUserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data["email"]
#             password = serializer.validated_data["password"]

#             # Create or save data to your queryset/model
#             # Replace 'YourModel' with your actual model
#             user_data = User.objects.create(email=email, password=password)

#             # You can perform other actions or return specific data as needed
#             # For example, returning the serialized data
#             return Response(
#                 {
#                     "message": "User created successfully",
#                     "data": serializer.validated_data,
#                 }
#             )

#         return Response(serializer.errors, status=400)


class RegisterApiView(CreateAPIView):
    # renderer_classes = [UserRenderer]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user_data = User.objects.create(
                email=email,
                username=username,
                password=make_password(password),
                is_active=False,
            )
            user_data.generate_verification_code()
            verification_code = user_data.verification_code
            send_mail(
                "کد تایید",
                f"کد تایید شما : {verification_code}",
                "your_email@gmail.com",
                [email],
                fail_silently=False,
            )

            return Response(
                {
                    "message1": "ثبت نام با موفقیت انجام شد",
                    "message2": "کد تایید به ایمل شما ارسال شد",
                    "data": serializer.validated_data["email"],
                }
            )

        return Response(serializer.errors, status=400)


class UserActivationView(GenericAPIView):
    # renderer_classes = [UserRenderer]

    def get(self, request, verification_code):
        try:
            user = User.objects.get(
                verification_code=verification_code, is_active=False
            )

            user.is_active = True
            user.save()
            return Response({"message": "احراز هویت شما به درستی انجام شد"})
        except user.DoesNotExist:
            return Response(
                {"message": "گد تایید اشتباه است"},
                status=status.HTTP_400_BAD_REQUEST,
            )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserLoginView(GenericAPIView):
    # renderer_classes = [UserRenderer]
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            user = authenticate(email=email, password=password)
            print(user, "user")
            if user is not None:
                if user.check_password(password) == False:
                    return Response({"message": "رمز عبور به درستی وارد نشده است"})
                if user.is_active == False:
                    return Response({"message": "شما احراز هویت نشده اید"})
                token = get_tokens_for_user(user)
                return Response({"message": "ورود با موفقیت انجام شد", "token": token})
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["کاربری با این ایمل وجود ندارد "]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=400)
