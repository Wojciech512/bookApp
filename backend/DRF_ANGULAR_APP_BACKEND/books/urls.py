from rest_framework import routers
from django.urls import include, path
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r"books", BookViewSet)
urlpatterns = [path("", include(router.urls))]
