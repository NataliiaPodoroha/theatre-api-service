from django.urls import path, include
from rest_framework import routers

from theatre_service.views import (
    ActorViewSet,
    GenreViewSet,
    PerformanceViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("performances", PerformanceViewSet)
router.register("plays", PlayViewSet)
router.register("reservations", ReservationViewSet)
router.register("theatre_halls", TheatreHallViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre_service"
