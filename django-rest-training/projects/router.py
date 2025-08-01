from rest_framework import routers
from .viewsets import ProjectViewSets

app_name = 'projects'

router = routers.DefaultRouter()
router.register(r'project', ProjectViewSets)