from django.urls import include, path
from .views import BookViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

drf_urlpatterns = [
    path('', include(router.urls))
]
