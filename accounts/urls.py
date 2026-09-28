from django.urls import path

from .views import LogoutView, MeView, RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("me/", MeView.as_view()),
    path("logout/", LogoutView.as_view()),
]