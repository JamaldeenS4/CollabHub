from django.urls import include, path
from rest_framework import routers

from .views import ProjectViewSet, TaskViewSet


router = routers.DefaultRouter()

router.register(r"projects", ProjectViewSet)
router.register(r"tasks", TaskViewSet)


urlpatterns = [
    path("", include(router.urls)),
]