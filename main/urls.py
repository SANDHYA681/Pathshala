"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from .views import *
from django.conf.urls.static import static
from main import settings
from users.views import *
from blogs.views import *

auth_urlpatterns = [
    path("log-in/", loginPage),
    path("sign-up/", signupPage),
    path("signin-user", loginUser),
    path("signup-user", signupUser),
    path("logout", logoutUser),
    path("edit-user", editUserPage),
    path("update-user", updateUser),
]

blog_urlpatterns = [
    path("add", addBlogPage),
    path("create", createBlog),
    path("<int:id>", blogDetails),          # blog/1
    path("edit/<int:id>", editBlog),    # blog/edit/1
    path("update/<int:id>", updateBlog),
]

writer_urlpatterns = [
    path("dashboard", dashboard),
    path("bloglist", blogList),  
]



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landingPage),
    path("about/", aboutPage),
    path("auth/", include(auth_urlpatterns)),
    path("blogs/", blogPage),
    path("profile/", profilePage),
    path("blog/", include(blog_urlpatterns)),
    path("writer/", include(writer_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
