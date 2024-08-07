"""interbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from renaper.views import DatosTemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin-interbase/', admin.site.urls),
    path('listado-interbase/', login_required(DatosTemplateView.as_view(template_name="datos_personas/listado.html")), name = 'listado-interbase'),
    path('detalle-interbase/<str:pk>/', login_required(DatosTemplateView.detalle_persona), name = 'detalle-interbase'),
    path('panel-interbase/', login_required(DatosTemplateView.panel_resumen), name = 'panel-interbase'),
    path('mapa-interbase/', login_required(DatosTemplateView.mapa_ubicaciones), name = 'mapa-interbase'),
    path('login-interbase/', DatosTemplateView.login, name = 'login-interbase'),
    path('logout-interbase/', DatosTemplateView.logout, name = 'logout-interbase'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
