from django.urls import include, path
from rest_framework import routers

from .views import TeamMembershipViewSet, TeamViewSet


router = routers.DefaultRouter()

router.register(r"teams", TeamViewSet)
router.register(r"memberships", TeamMembershipViewSet)


urlpatterns = [
    path("", include(router.urls)),
]