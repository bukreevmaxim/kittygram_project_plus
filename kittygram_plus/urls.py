from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owner', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]