from django.urls import path
from .views import LoginView, RegisterView, MeView, PerfilListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', MeView.as_view(), name='me'),
    path('perfis/', PerfilListView.as_view(), name='perfis'),
]
