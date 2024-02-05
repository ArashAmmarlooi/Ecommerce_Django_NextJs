from django.urls import path, re_path
from . import views

app_name = "Ecommerce"

urlpatterns = [
    path("/v1/register", views.RegisterApiView.as_view()),
    path("/v1/activate/<str:verification_code>", views.UserActivationView.as_view()),
    path("/v1/login", views.UserLoginView.as_view()),
    # re_path(
    #     r"/v1/products/(?P<slug>[^/]+)/?$",
    #     views.ProductsByCategory.as_view(),
    #     name="Category",
    # ),
    # path("/v1/search", views.ProductsByQuery.as_view()),
    #     path(
    #     "api/v1/products/(?P<name>[-\w]+)/",
    #     views.ProductsByCategory.as_view(),
    #     name="category_item",
    # ),
    # path(
    #     "re_path(r'^(?P<str:slug>[-\w]*)/$'",
    #     views.ProductsByCategory.as_view(),
    #     name="category_item",
    # ),
    # path(
    #     "re_path(r'(?P<str:slug>[^/]+)/?$'",
    #     views.ProductsByCategory.as_view(),
    #     name="category_item",
    # ),
    # re_path(r"api/v1/course/(?P<name>[-\w]+)/", views.CourseDetail.as_view()),
    # path("api/v1/blogs", views.BlogList.as_view()),
    # path("api/v1/blog/<str:name>", views.BlogDetail.as_view()),
]
