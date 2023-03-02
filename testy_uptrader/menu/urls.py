from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from menu.views import root


urlpatterns = [
    path('', root, name='root'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
