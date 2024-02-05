from django.urls import path, re_path
from . import views

app_name = "Ecommerce"

urlpatterns = [
    path("/v1/category", views.Categorylist.as_view()),
    path("/v1/subcategory", views.SubCategorylist.as_view()),
    path("/v1/products", views.ProductList.as_view()),
    path("/v1/product/<int:pk>", views.ProductDetail.as_view()),
    re_path(
        r"/v1/products/(?P<slug>[^/]+)/?$",
        views.ProductsByCategory.as_view(),
        name="Category",
    ),
    re_path(
        r"/v1/products/(?P<catslug>[^/]+)/(?P<subslug>[^/]+)/?$",
        views.ProductsBySubCategory.as_view(),
        name="subcategory_search",
    ),
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
