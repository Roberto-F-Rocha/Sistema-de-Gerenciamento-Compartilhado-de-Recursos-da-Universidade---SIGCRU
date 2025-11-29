from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('patrimonios.urls')),
    path('api/', include('manutencoes.urls')),
    path("api/solicitacoes/", include("solicitacoes.api.urls")),
    path('api/users/', include('users.api.urls')),
]
