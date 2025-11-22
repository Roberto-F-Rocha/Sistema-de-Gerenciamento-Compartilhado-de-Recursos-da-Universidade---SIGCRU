from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('patrimonios.urls')),
    path('api/', include('manutencoes.urls')),
    path('api/', include('solicitacoes.urls')),
    path('api/users/', include('users.api.urls')),

]
