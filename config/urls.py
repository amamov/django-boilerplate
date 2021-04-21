from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
        path("__debug__/", include(debug_toolbar.urls))
    ]
