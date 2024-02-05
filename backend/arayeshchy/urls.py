from argparse import Namespace
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

# import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", include("Ecommerce.urls")),
    path("api", include("account.urls")),
    # path("__debug__/", include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     path("__debug__/", include(debug_toolbar.urls)),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
