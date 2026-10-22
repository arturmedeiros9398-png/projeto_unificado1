from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView
from config.api_root import api_root

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Root - lista todos os endpoints
    path('api/', api_root, name='api-root'),

    # Auth
    path('api/auth/', include('apps.users.urls')),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Comum
    path('api/comum/', include('apps.comum.urls')),

    # Módulos
    path('api/drogas/', include('apps.drogas.urls')),
    path('api/saude-mental/', include('apps.saude_mental.urls')),
    path('api/qualidade-vida/', include('apps.qualidade_vida.urls')),

    # Documentação
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]