from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'user', views.UserViewSet, basename='user')
router.register(r'profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls))
]