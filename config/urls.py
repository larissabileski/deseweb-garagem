from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet
from garagem.views import MarcaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marca", MarcaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]