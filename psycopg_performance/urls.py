import debug_toolbar

from django.urls import path, include

from .views import index, generate

urlpatterns = [
    path("", index),
    path("generate/", generate),
    path("__debug__/", include(debug_toolbar.urls)),
]
