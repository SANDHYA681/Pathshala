from django.contrib import admin
from django.urls import include, path
from users.router import router as user_router
from projects.router import router as project_router

from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path('users/', include(user_router.urls)),
    path('projects/', include(project_router.urls)),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]

#
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
