from rest_framework import routers
from .viewsets import *

app_name = "users"

router = routers.DefaultRouter()
router.register('user', UserViewSet)        # Handles /api/users/user/
router.register('profile', ProfileViewSet)  # Handles /api/users/profile/
