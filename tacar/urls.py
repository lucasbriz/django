"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from core.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('', home, name='url_principal'),
    #Cadastros
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('cadastro_fabricante/', cadastro_fabricante, name='url_cadastro_fabricante'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('cadastro_tabela/', cadastro_tabela, name='url_cadastro_tabela'),
    #Listas
    path('lista_clientes/', lista_clientes, name='url_lista_clientes'),
    path('lista_veiculos/', lista_veiculos, name='url_lista_veiculos'),
    path('lista_fabricantes/', lista_fabricantes, name='url_lista_fabricantes'),
    path('lista_rotativos/', listagem_rotativos, name='url_listagem_rotativos'),
    path('lista_mensalistas/', lista_mensalista, name='url_lista_mensalistas'),

    path('tabela_precos/', lista_tabela, name='url_tabela_precos'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_lista_clientes'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_lista_clientes'),
    path('alterar_rotativo/<int:id>/', alterar_rotativo, name='url_alterar_rotativo'),
    path('alterar_mensalista/<int:id>/', alterar_mensalista, name='url_alterar_mensalista'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
