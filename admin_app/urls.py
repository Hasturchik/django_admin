from django.urls import include, path
from rest_framework import routers
from .views import StationViewSet

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)

urlpatterns = [
    path('', include(router.urls)),

]