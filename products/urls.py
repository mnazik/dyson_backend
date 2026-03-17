from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Dyson API",
        default_version='v1',
        description="API documentation for Dyson backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Router
product_router = DefaultRouter()
product_router.register(r'products', ProductViewSet)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]