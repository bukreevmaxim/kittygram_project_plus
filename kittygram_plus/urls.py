from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcat')

urlpatterns = [
    path('', include(router.urls)),
]