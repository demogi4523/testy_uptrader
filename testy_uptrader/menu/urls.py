from django.urls import path

from menu.views import root


urlpatterns = [
    path('', root, name='root'),
]
