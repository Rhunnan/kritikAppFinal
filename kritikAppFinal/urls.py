
from django.contrib import admin
from django.urls import include, path
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/', include(router.urls)),
]
