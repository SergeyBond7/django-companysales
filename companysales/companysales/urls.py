from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from config.views import home

urlpatterns = [
    path('', include('config.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('config.urls')),
    path('', home)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
