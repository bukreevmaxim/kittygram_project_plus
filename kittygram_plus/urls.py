from django.urls import include, path

# from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcat')

urlpatterns = [
    path('', include(router.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
    
    # path('api-token-auth/', views.obtain_auth_token),
]